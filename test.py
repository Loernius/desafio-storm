import unittest
import desafio
class TestCases(unittest.TestCase):

    facts_working = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]
    facts_with_error = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]
    schema_working = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ]
    schema_with_error = [
        ('endereço', 'cardinality'),
        ('telefone', 'cardinality', 'many')
    ]
    schema_with_not_supported_cardinality = [
        ('endereço', 'cardinality', 'two'),
        ('telefone', 'cardinality', 'many')
    ]
    def testNormalCase(self):
        self.assertEquals(desafio.returnActualFacts(self.facts_working, self.schema_working), {
            "success": True,
            "facts": [
                ('gabriel', 'endereço', 'av rio branco, 109', True), 
                ('joão', 'endereço', 'rua bob, 88', True), 
                ('joão', 'telefone', '234-5678', True), 
                ('joão', 'telefone', '91234-5555', True), 
                ('gabriel', 'telefone', '98888-1111', True), 
                ('gabriel', 'telefone', '56789-1010', True)
            ]
        })
    def testErrorFacts(self):
        self.assertEquals(desafio.returnActualFacts(self.facts_with_error, self.schema_working), {
            "success": False,
            "message": "Error on facts structure"
        })
    def testErrorSchema(self):
        self.assertEquals(desafio.returnActualFacts(self.facts_working, self.schema_with_error), {
            "success": False,
            "message": "Error on schema structure"
        })
    def testErrorSchemaCardinality(self):
        self.assertEquals(desafio.returnActualFacts(self.facts_working, self.schema_with_not_supported_cardinality), {
            "success": False,
            "message": "Unsupported cardinality"
        })


if __name__ == '__main__':
    unittest.main()

