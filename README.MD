```markdown
# Curie CLI

Command-line interface for the [Curie](https://curie.sh) scientific AI platform. Run biology, chemistry, and physics models directly from your terminal.

## Installation

```bash
pip install curie-cli
```

## Authentication

```bash
curie auth login
```

Or set your API key as an environment variable:

```bash
export CURIE_API_KEY="sk-..."
```

Get your API key at [curie.sh/dashboard/keys](https://curie.sh/dashboard/keys). First 500 calls are free.

## Commands

### Fold a protein
```bash
curie fold MKTIIALSYIFCLVFA
curie fold MKTIIALSYIFCLVFA --output structure.pdb
```

### Dock a small molecule
```bash
curie dock --protein structure.pdb --ligand "CC(=O)Oc1ccccc1C(=O)O"
curie dock --protein structure.pdb --ligand aspirin.sml --output pose.pdb
```

### Generate embeddings
```bash
curie embed MKTIIALSYIFCLVFA
curie embed MKTIIALSYIFCLVFA --output embeddings.json
```

### List available models
```bash
curie models
curie models --domain biology
```

## Models

| Model | Domain | Description | Latency |
|---|---|---|---|
| `esm/esmfold-v1` | Biology | Protein structure prediction | ~200ms |
| `mit/boltz-2` | Biology | Biomolecular complex prediction | ~2min |
| `baker/proteinmpnn` | Biology | Protein sequence design | ~300ms |
| `meta/esm-2-650m` | Biology | Protein language model embeddings | ~90ms |
| `mit/diffdock` | Chemistry | Molecular docking | ~800ms |

## Links

- [Documentation](https://curie.sh/docs)
- [Model Catalog](https://curie.sh/models)
- [Dashboard](https://curie.sh/dashboard)
- [Status](https://status.curie.sh)

## License

MIT — see [LICENSE](LICENSE)
```