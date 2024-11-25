def substituir_nulo(valor, padrao):
    """
    Substitui o valor por um padrão caso seja None, para evitar inserção de dados nulos em um banco de dados.

    Parâmetros:
        valor: O valor que será verificado.
        padrao: O valor padrão que será usado caso 'valor' seja None.

    Retorno:
        O 'valor' se ele não for None; caso contrário, retorna 'padrao'.
    """
    return padrao if valor is None else valor
