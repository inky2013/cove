# Deployment Notes

General Django deployment considerations apply to deploying Cove. We deploy using Apache and uwsgi using this  [Salt State file](https://github.com/OpenDataServices/opendataservices-deploy/blob/master/salt/cove.sls).

## How to create a deployment pull request


Post a pull request with a title following the appropriate template.:

For the monthly rollout of new features:
```
End of {{Month}} {{Year}} live deployment 
```

For bug fixes:
``
Post {{Month}} {{Year}} bug fixes ({{Num}}) - {{optionally, brief description of changes}} - live deployment 
``

In both cases, add a description following this template:
```
URL for testing: http://release-{{YYYYMM}}.dev.cove.opendataservices.coop/

Planned deployment date: 

#### Summary of changes for this deployment

#### Tasks in deploy process

Before merge:
- [ ] Re-run translations if any text has changed
- [ ] Create a new branch `release-{{YYYYMM}}` if it doesn't exist.
- [ ] Deploy to a subdomain on the dev server http://release-{{YYYYMM}}.dev.cove.opendataservices.coop/ - redo this for any additional commits
- [ ] Check that the correct commit has been deployed using the link in the footer http://release-{{YYYYMM}}.dev.cove.opendataservices.coop/
- [ ] Run `CUSTOM_SERVER_URL=http://release-{{YYYYMM}}.dev.cove.opendataservices.coop/ py.test fts` - redo this for each redeploy to the subomdain

After merge:
- [ ] Run salt highstate on `cove-live`
- [ ] Check that the correct commit has been deployed using the link in the footer http://cove.opendataservices.coop/
- [ ] Run `CUSTOM_SERVER_URL=http://cove.opendataservices.coop/ PREFIX_360=/360/ py.test fts` on a local copy of the updated live branch
- [ ] Run salt highstate on `cove-live-ocds`
- [ ] Check that the correct commit has been deployed using the link in the footer http://standard.open-contracting.org/validator/
- [ ] Run `CUSTOM_SERVER_URL=http://standard.open-contracting.org PREFIX_OCDS=/validator/ py.test fts ` on a local copy of the updated live branch
- [ ] Check that changes on live are merged back into master too
```

Where `{{YYYYMM}}` should be replace with the actual year and month numbers - e.g. 201602

Add any extra tasks as appropriate. If they should be recurring update this template.
