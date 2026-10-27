# Kit de documentação para projetos de software

Estrutura inicial de documentação para copiar ou adaptar em um repositório de software. Os documentos estão em português.

## Estrutura

```text
docs/
├── README.md
├── adr/
│   ├── README.md
│   └── adr-template.md
├── specs/
│   └── spec-template.md
├── runbooks/
│   └── runbook-template.md
└── guides/
    └── praticas.md
```

## Como começar

1. Copie a pasta `docs/` para o repositório do projeto.
2. Leia [`docs/guides/praticas.md`](docs/guides/praticas.md) e ajuste as convenções à equipe.
3. Para uma mudança com requisitos ou coordenação, copie [`docs/specs/spec-template.md`](docs/specs/spec-template.md) para um arquivo `AAAA-MM-DD-assunto.md`.
4. Para uma decisão técnica duradoura, use [`docs/adr/adr-template.md`](docs/adr/adr-template.md) e numere o arquivo como `NNNN-titulo-curto.md`.
5. Para operação ou recuperação de serviço, copie [`docs/runbooks/runbook-template.md`](docs/runbooks/runbook-template.md) e documente passos verificáveis.

A documentação deve acompanhar o código e ser revisada junto com as mudanças relacionadas.
