# Repository Maintenance Checklist

Use this checklist when refreshing the public model/API information.

## Catalog and examples

- [ ] Confirm the live landing page and exact model IDs.
- [ ] Compare every input field and modality with the current endpoint schema.
- [ ] Check input and output rates; date every price snapshot.
- [ ] Confirm the submit response, prediction status values, and output shape.
- [ ] Review streaming behavior against the current endpoint documentation.
- [ ] Run through the cURL, Python, and JavaScript examples with a development API key. Never record the key or private prompt in the repository.
- [ ] Check all Muapi links and account/access paths.

## GitHub metadata

- [ ] Keep the repository public and on the `main` default branch.
- [ ] Keep its description focused on the Muapi abliterated API guide.
- [ ] Use no more than 20 relevant topics.
- [ ] Keep `README.md`'s `Related Projects` section immediately before the first other level-two section.
- [ ] Review the MIT license notice and product/model attribution.
- [ ] Confirm a fresh clone contains the examples, docs, license, and issue/security guidance.
