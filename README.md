# Documentação do projeto

Esta pasta reúne a documentação mantida junto ao código do projeto. Para usar este kit em outro repositório, copie o conteúdo deste diretório para a pasta `docs/` do projeto de destino. Copie `README.md` e as pastas `adr/`, `specs/`, `runbooks/` e `guides/`; não é necessário criar uma pasta `docs/` dentro dela.

## Navegação

- `adr/`: decisões arquiteturais e técnicas com consequências duradouras.
- `specs/`: requisitos e propostas de mudanças relevantes.
- `runbooks/`: procedimentos de operação, diagnóstico e recuperação.
- `guides/`: instruções conceituais ou de desenvolvimento que atravessam várias mudanças.

## Como começar

1. Leia [as boas práticas de documentação](guides/praticas.md) e ajuste as convenções à equipe.
2. Para uma mudança com requisitos ou coordenação, copie [o template de Spec](specs/spec-template.md) para um arquivo `AAAA-MM-DD-assunto.md`.
3. Para uma decisão técnica duradoura, use [o template de ADR](adr/adr-template.md) e numere o arquivo como `NNNN-titulo-curto.md`.
4. Para operação ou recuperação de serviço, copie [o template de runbook](runbooks/runbook-template.md) e documente passos verificáveis.

## Convenções

- Use Markdown e links relativos para documentos nesta pasta.
- Nomeie ADRs com número sequencial e título: `NNNN-titulo-curto.md`.
- Nomeie Specs com data e assunto: `AAAA-MM-DD-assunto.md`.
- Inclua estado, responsável e links relacionados nos documentos sujeitos a revisão.
- Marque documentos substituídos como tal e aponte para o substituto; evite apagar o histórico decisório.

A documentação deve acompanhar o código e ser revisada junto com as mudanças relacionadas. Mantenha aqui as instruções específicas do projeto, como responsáveis e fluxo de aprovação.
