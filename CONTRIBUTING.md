# Contributing

## Conventional Commits

Format : `type(scope): description courte`

### Types
- `feat` — nouvelle fonctionnalité
- `fix` — correction de bug
- `ci` — modification du pipeline CI/CD
- `test` — ajout ou modification de tests
- `refactor` — refactoring sans changement de comportement
- `chore` — maintenance, config, dépendances
- `docs` — documentation

### Scope
Ce qui est impacté : `app`, `ci`, `docker`, `k8s`, `workflow`

### Exemples
- `feat(app): externalize SECRET_KEY via env var`
- `fix(ci): add fetch-depth 0 for gitleaks`
- `ci(workflow): add pytest job`
- `test(app): fix nosemgrep for TESTING flag`