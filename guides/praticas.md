# Boas práticas de documentação de software

## Escolha o documento pela pergunta

- **ADR:** “Que decisão tomamos, por que, e quais efeitos esperamos?” Use para escolhas difíceis de reverter ou que afetam várias pessoas, sistemas ou mudanças futuras. Um ADR registra uma decisão, não uma especificação inteira.
- **Spec:** “O que precisa mudar e como saberemos que está correto?” Use para mudanças com múltiplos requisitos, colaboração entre funções, riscos ou alternativas de desenho. Uma Spec pode apontar para vários ADRs.
- **Runbook:** “Como operar, diagnosticar ou recuperar o serviço?” Escreva para quem está sob pressão, com passos verificáveis e links úteis.
- **Guia:** “Como fazemos esta atividade recorrente?” Use para conhecimento estável que não pertence a uma única entrega.
- **README:** “O que é este projeto e como começo?” Mantenha a entrada curta e direcione para detalhes.

## ADRs que continuam úteis

- Escreva o contexto antes da decisão: restrições e forças tornam a escolha compreensível no futuro.
- Registre alternativas plausíveis e os motivos da escolha; evite listas artificiais de opções que nunca foram consideradas.
- Prefira decisões atômicas. Se há duas decisões independentes, crie dois ADRs e faça links entre eles.
- Dê estado explícito. Ao mudar a decisão, crie um novo ADR que substitua o anterior e ligue os dois.
- Registre consequências positivas e negativas, incluindo custo operacional e dívida assumida.
- Não reescreva a história para fazê-la parecer inevitável; mantenha o registro fiel ao que era conhecido na época.

## Specs acionáveis

- Comece pelo problema e pelas pessoas ou sistemas afetados, não pela solução preferida.
- Separe objetivos de fora de escopo para evitar expansão silenciosa.
- Escreva critérios de aceitação observáveis. Prefira “dado/quando/então” a termos vagos como “rápido” ou “seguro”.
- Separe comportamento necessário de detalhes de implementação que ainda podem mudar.
- Aponte incertezas explicitamente e dê responsável ou condição de resolução.
- Inclua implantação, compatibilidade, migração, observabilidade e rollback quando forem relevantes.
- Mantenha o documento atualizado durante a implementação; registre alterações materiais e decisões em ADRs.

## Manutenção e fluxo de trabalho

- Guarde documentos no mesmo repositório do código relacionado quando possível; isso facilita revisão e histórico conjunto.
- Faça revisão documental em pull requests como parte da revisão da mudança, com o nível de detalhe proporcional ao risco.
- Não documente cada linha de código: nomes claros, tipos, testes e comentários locais explicam detalhes de implementação melhor. Documente intenção, contratos, limites e razões não óbvias.
- Evite duplicar a mesma informação em vários lugares. Escolha uma fonte principal e faça links.
- Use linguagem direta, termos consistentes, exemplos pequenos e datas em formato ISO (`AAAA-MM-DD`).
- Defina revisão para documentos operacionais ou sujeitos a mudança. Arquive ou marque como substituído o conteúdo obsoleto, e corrija instruções perigosas assim que forem detectadas.
- Não inclua senhas, tokens, dados pessoais ou informação restrita em documentos versionados.

## Um fluxo leve sugerido

1. Mudança pequena e local: issue/PR com contexto e validação; sem documento separado se não agregar valor.
2. Mudança com requisitos ou coordenação: rascunho de Spec, revisão, implementação e atualização da Spec para refletir o resultado.
3. Escolha arquitetural relevante durante a Spec: ADR separado, ligado à Spec.
4. Mudança que afeta operação: atualize ou crie runbook, alertas e instruções de rollback.
5. Após entrega: marque Spec como concluída e deixe links para a implementação e decisões.

A equipe pode simplificar ou ampliar esse fluxo conforme risco, regulação e escala. O objetivo é reduzir perda de contexto e retrabalho, não maximizar a quantidade de páginas.
