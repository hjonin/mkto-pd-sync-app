# Sync App

Synchronize data between Marketo and Pipedrive.

## marketo module

Simple Python client for the Marketo REST API.

### Main features

Lead, opportunities, roles and companies are classes that can be instantiated given a Marketo client instance.

All fields are loaded and available for reading and a defined subset for each resource is available for updating.

A resource also has an "id field" that will be used to match an existing resource.

An existing resource can be loaded given an identifier and an eventual id field to look for different from its actual one
which can be any exiting field for leads but should be a "searchable field" for opportunities, roles and companies.

A resource can be saved: it is then created or updated depending on if it matches an existing one.

### Usage

```python
import marketo

mkto = marketo.MarketoClient(IDENTITY_ENDPOINT, CLIENT_ID, CLIENT_SECRET, API_ENDPOINT)

# Get a lead by id
lead = marketo.Lead(mkto, "12345")

# Get a lead by email
lead = marketo.Lead(mkto, "lead@mail.com", "email")

# Update lead data
lead.firstName = "New Name"
lead.save()
```

## pipedrive module

Simple Python client for the Pipedrive REST API.

### Main features

People, organizations and deals are classes that can be instantiated given a Pipedrive client instance.

All fields are loaded and available for reading and updating.

An existing resource can be loaded given an identifier or a name if the "id field" parameter is given as "name".

Custom fields can be read using a nicer name (snake case display name) than their hash key.

Some resources are related to other and can be loaded as well if so.

A resource can be saved: it is then created or updated depending on if it matches an existing one.

For related resources, only the link can be updated.

### Usage

```python
import pipedrive

pd = pipedrive.PipedriveClient(secret.PD_API_TOKEN)

# Get a person by id
person = pipedrive.Person(pd, "12345")

# Get an organization by name
organization = pipedrive.Organization(pd, "MyCompany", "name")

# Get a person custom field with its nicer name
person.lead_score  # or getattr(person, {HASH KEY})

# Get a person related organization
organization = person.organization

# Update person data
person.name = "New Name"
person.save()
```

## sync module

Simple Flask app to synchronize data between Marketo and Pipedrive.

### Main features

#### Endpoints

5 endpoints accessible through a POST request:
- `/marketo/lead/<int:lead_id>`: to send lead data from Marketo to Pipedrive

Actually synchronizes data if and only if it is new or it has changed.

- `/pipedrive/person/<int:person_id>`: to send person data from Pipedrive to Marketo

Actually synchronizes data if and only if it is new or it has changed.

- `/pipedrive/deal/<int:deal_id>`: to send deal data from Pipedrive to Marketo

Actually synchronizes data if and only if it is new or it has changed.

- `/marketo/lead/<int:lead_pipedrive_id>/delete`: to delete a person in Pipedrive (using lead pipedrive id)

- `/pipedrive/person/<int:pipedrive_marketo_id>/delete`: to delete a lead in Marketo (using person marketo id)

#### Authentication

All routes require authentication using an API key as GET parameter.

#### Mapping

A mapping file describes how Marketo and Pipedrive resource fields should be matched.

##### Schema
```
MAPPING_NAME = {
    to_field_key_1: {
        "fields": [from_field_key_1, [from_field_key_2...]],
        ["mode": "join"/"choose",]
        ["pre_adapter": function,]
        ["post_adapter": function]
    },
    to_field_key_2: {
        "transformer": function
    }
}
```

### Usage

Any call returns the synchronisation status ("created", "updated" or "skipped") as well as the id of the created/updated resource in JSON.

## Testing

Marketo and Pipedrive clients are tested in the tests module, as well as the sync app.
