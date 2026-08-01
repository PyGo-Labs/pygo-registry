# PyGo Registry

Official module registry for PyGo Framework.

## 📦 What is the PyGo Registry?

The **PyGo Registry** is the central catalog of official and community modules for the PyGo ecosystem. It provides:

- A static `registry.json` file listing all available modules
- GitHub Actions for validation of new module submissions
- Documentation for module authors on how to publish

## 🏗️ Architecture

This registry is intentionally **static** — it uses a single `registry.json` file served via GitHub's CDN. No servers, no database, zero maintenance.

| Component | Technology |
|-----------|-----------|
| Registry data | `registry.json` (static JSON) |
| Validation | GitHub Actions (Python) |
| Distribution | GitHub raw.githubusercontent.com CDN |
| Cost | $0 |

## 📁 Structure

```
pygo-registry/
├── registry.json           # The registry catalog
├── modules/                # Module metadata (future)
├── scripts/                # Validation scripts
├── .github/workflows/      # CI/CD validation
├── CONTRIBUTING.md         # How to publish modules
└── README.md
```

## 📄 registry.json Format

```json
{
  "version": "1.0",
  "modules": [
    {
      "name": "my-module",
      "version": "1.0.0",
      "description": "A PyGo module",
      "author": "your-github-username",
      "repository": "https://github.com/your/repo",
      "download_url": "https://github.com/your/repo/releases/download/v1.0.0/module.tar.gz",
      "checksum": "sha256:abc123...",
      "dependencies": ["pygo-framework>=1.0.0"],
      "license": "MIT",
      "category": "ui",
      "tags": ["tag1", "tag2"],
      "official": true
    }
  ]
}
```

## 🤝 How to Publish a Module

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide.

## 🔗 Related Projects

- [PyGo Framework](https://github.com/pygo-labs/pygo-framework) — The core framework
- [PyGo UI](https://github.com/pygo-labs/pygo-ui) — Official UI components
- [PyGo Admin](https://github.com/pygo-labs/pygo-admin) — Admin dashboard components
- [PyGo Auth](https://github.com/pygo-labs/pygo-auth) — Authentication module

## 📜 License

MIT — See [LICENSE](./LICENSE)
