# Resumo de Pandas

>Por convensão e afim de tornar possiveis duvidas mais fáceis de serem localizadas futuramente em buscas em sites como Stackoverflow e derivados, vamos adotar a biblioteca **pandas como pd**

```py
import pandas as pd
```

## Series (Colunas)

- Series são como as tabelas do excel e são como as suas linhas e podem ser passados da seguinte forma:

```py
    import pandas as pd
    minha_serie = pd.Series(valores,indices)
```

**pd.Series(x,y)**


|atributos da funcao|
---|
|x = data|
|y = index|



|Indice|Valor|
---|---
|0|'a'|
|1|'b'|
|2|'c'|