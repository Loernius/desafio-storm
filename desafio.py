# Desafio Backend Python
# Considere um modelo de informação, onde um registro é representado por uma "tupla".
# Uma tupla (ou lista) nesse contexto é chamado de fato.
# Exemplo de um fato:
# ('joão', 'idade', 18, True)
# Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.
# Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False'
# para representar que a entidade não tem mais aquele valor associado aquele atributo.
# Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).
# Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)
facts = [
    ('gabriel', 'endereço', 'av rio branco, 109', True),
    ('joão', 'endereço', 'rua alice, 10', True),
    ('joão', 'endereço', 'rua bob, 88', True),
    ('joão', 'telefone', '234-5678', True),
    ('joão', 'telefone', '91234-5555', True),
    ('joão', 'telefone', '234-5678', False),
    ('gabriel', 'telefone', '98888-1111', True),
    ('gabriel', 'telefone', '56789-1010', True),
]
# Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.
# Nesse schema,
# o atributo 'telefone' tem cardinalidade 'muitos' (one-tomany), e 'endereço' é 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]
# Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:
# (
# ('joão', 'endereço', 'rua alice, 10', True)
# ('joão', 'endereço', 'rua bob, 88', True),
#)
# E o fato considerado vigente (ou ativo) é o último.
# O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.
# Ou seja, quais são as informações que estão valendo no momento atual.
# A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.
# Resultado esperado para este exemplo (mas não precisa ser nessa ordem):
# [
# ('gabriel', 'endereço', 'av rio branco, 109', True),
# ('joão', 'endereço', 'rua bob, 88', True),
# ('joão', 'telefone', '91234-5555', True),
# ('gabriel', 'telefone', '98888-1111', True),
# ('gabriel', 'telefone', '56789-1010', True)
# ]

import pandas as pd

def returnActualFacts(facts, schema):

    for row in schema:
        if len(row) != 3:
            returnObject = {
                "success": False,
                "message": "Error on schema structure"
            }

            print(returnObject)
            return returnObject
    for row in facts:
        if len(row) != 4:
            returnObject = {
                "success": False,
                "message": "Error on facts structure"
            }

            print(returnObject)
            return returnObject
    schema_data = pd.DataFrame(schema)
    schema_data.columns = ["data_column", "cardinality_ref", "cardinality_type"]
    
    facts_data = pd.DataFrame(facts)
    facts_data.columns = ["name", "type", "data_from_type", "active"]

    active_facts_data = facts_data[facts_data["active"] == True]
    factsSelected = []
    for row in schema_data.values:
        data_type = row[0]
        cardinality = row[2]
        selected_data = active_facts_data[active_facts_data["type"] == data_type]
            
        if cardinality == 'one':
            for name in selected_data.name.unique():
                data_by_name = selected_data[selected_data.name == name]
                last_ocorrence = data_by_name.to_numpy()[-1]
                factsSelected.append(tuple(last_ocorrence))
        elif cardinality == 'many':
            for x in selected_data.to_numpy():
                factsSelected.append(tuple(x))
        else:
            returnObject = {
                "success": False,
                "message": "Unsupported cardinality"
            }
            return returnObject


    print(factsSelected)
    returnObject = {
        "success": True,
        "facts": factsSelected
    }
    return returnObject
    


if __name__ == '__main__':
    returnActualFacts(facts, schema)