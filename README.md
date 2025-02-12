# FP 23/24 - Projeto 1
**Filipe Oliveira**  
**Número de estudante**: ist1110633

## Descrição do Projeto
O seguinte código contém uma série de funções que permitem obter algumas informações sobre o estado de um território retangular formado por caminhos verticais e horizontais. As interseções dos caminhos de um território podem ou não estar ocupadas por montanhas, formando cadeias de montanhas e vales.

## Termos

### Território
- Estrutura retangular formada por:
  - **Caminhos verticais** (identificados de 'A' a 'Z', no máximo).
  - **Caminhos horizontais** (identificados por um número inteiro de 1 a 99, no máximo).

### Interseção
- Ponto no território onde um caminho vertical encontra um caminho horizontal.

### Interseções adjacentes
- Interseções conectadas por um caminho vertical/horizontal sem outras interseções entre elas.

### Interseção livre
- Interseção não ocupada por montanhas.

### Interseções conectadas
- Interseções do mesmo tipo em que é possível traçar um percurso entre elas, passando sempre por interseções do mesmo tipo.

### Cadeia de montanhas
- Conjunto de uma ou mais montanhas conectadas entre si e não conectadas a nenhuma outra montanha.

### Cadeia de interseções livres
- Conjunto de uma ou mais interseções livres conectadas entre si e não conectadas a nenhuma outra interseção livre.

### Vale de uma montanha
- Conjunto de interseções livres adjacentes a essa montanha ou adjacente a uma montanha da mesma cadeia de montanhas.