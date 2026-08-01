# Contributing to the PyGo Registry

## How to Add a Module

1. Fork the `pygo-labs/pygo-registry` repository
2. Edit `registry.json` to add your module entry
3. Submit a pull request
4. GitHub Actions will validate your submission
5. A maintainer will review and merge

## Module Requirements

Each module entry must include:

| Field | Required | Description |
|-------|----------|-------------|
| `name` | ✅ | Unique module name (lowercase, hyphens) |
| `version` | ✅ | Semver version (e.g., `1.0.0`) |
| `description` | ✅ | Short description (< 200 chars) |
| `author` | ✅ | Your GitHub username |
| `repository` | ✅ | GitHub URL (e.g., `https://github.com/your/repo`) |
| `license` | ✅ | SPDX license identifier (e.g., `MIT`, `AGPL-3.0`) |
| `category` | ✅ | One of: `ui`, `admin`, `backend`, `devtools`, `utils`, `other` |
| `download_url` | ⚠️ | HTTPS URL to the release tarball/zip |
| `checksum` | ⚠️ | SHA256 checksum of the release artifact |
| `dependencies` | ⚠️ | Array of required dependencies |
| `tags` | ❌ | Array of tags for search |
| `official` | ❌ | `true` if published by PyGo Labs |

## Validation Rules

The GitHub Actions workflow validates:

- ✅ JSON syntax is valid
- ✅ All required fields are present
- ✅ No duplicate module names
- ✅ Version follows semver format
- ✅ Repository URL is a valid GitHub URL
- ✅ Download URL is HTTPS (if provided)

## Publishing Your Module

1. **Create a release** on your module's GitHub repo
2. **Tag it** with a semver version (e.g., `v1.0.0`)
3. **Upload** your module as a `.tar.gz` artifact
4. **Get the SHA256 checksum**:
   ```bash
   shasum -a 256 your-module-1.0.0.tar.gz
   ```
5. **Add your entry** to `registry.json` with the download URL and checksum

## Questions?

Join us on [Telegram](https://t.me/pygo_foundation) or open an issue.
