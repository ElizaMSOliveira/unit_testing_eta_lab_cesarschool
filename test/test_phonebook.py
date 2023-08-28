from src.phonebook import Phonebook


class TestPhonebook:


    def test_add_com_sucesso(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Numero adicionado"
        # Chamada
        resultado = phone.add("SAMU", "180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_hashtag(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.add("SAMU#", "180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_at(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.add("SAMU@", "180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_exclamation(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.add("SAMU!", "180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_cifrao(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.add("SAMU$", "180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_percentage(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.add("SAMU%", "180""")
        # Avaliação
        assert resultado == resultado_esperado

    def test_add_com_failure_numero_vazio(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Numero invalido"
        # Chamada
        resultado = phone.add("SAMU", "")
        # Avaliação
        assert resultado == resultado_esperado

    def test_lookup_success(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "190"
        # Chamada
        resultado = phone.lookup("POLICIA")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_failed(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome Não Encontrado"
        # Chamada
        resultado = phone.lookup("OLICA")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_com_failure_hashtag(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invaldo"
        # Chamada
        resultado = phone.lookup("POLICIA#")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_com_failure_at(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.lookup("@POLICIA")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_com_failure_exclamation(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.lookup("POL!CIA")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_com_failure_cifrao(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.lookup("POLICI$")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_lookup_com_failure_percentage(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Nome invalido"
        # Chamada
        resultado = phone.lookup("%POLICIA")
        # Avaliacao
        assert resultado == resultado_esperado

    def test_get_names(self):
        # Setup
        phone = Phonebook()
        resulto_esperado = ["POLICIA"]
        # Chamada
        resultado = phone.get_names()
        # Validação
        assert resultado == resulto_esperado

    def test_getnumber(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = ["190"]
        # Chamada
        resultado = phone.get_numbers()
        # Avaliação
        assert resultado == resultado_esperado

    def test_clear(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "phonebook limpado"
        # Chamada
        resultado = phone.clear()
        #Avaliação
        assert resultado == resultado_esperado

    def test_secarch_success(self):
        # Setup
        phone = Phonebook()
        ressultado_esperado = [{"POLICIA", "190"}]
        # Chamada
        ressultado = phone.search("POLICIA")
        # Avaliação
        assert ressultado == ressultado_esperado

    def test_secarch_failed(self):
        # Setup
        phone = Phonebook()
        ressultado_esperado = "Name not found"
        # Chamada
        ressultado = phone.search("POLICA")
        # Avaliação
        assert ressultado == ressultado_esperado

    def test_get_phonebook_sorted(self):
        # Setup
        phone = Phonebook()
        phone.add("SAMU", "193")
        phone.add("BOMBEIRO", "192")
        resultado_esperado = [("BOMBEIRO", "192"), ("POLICIA", "190"), ("SAMU", "193")]
        # Chamada
        resultado = phone.get_phonebook_sorted()
        # Avaliação
        assert resultado == resultado_esperado

    def test_phonebook_reverse(self):
        # Setup
        phone = Phonebook()
        phone.add("SAMU", "193")
        phone.add("BOMBEIRO", "192")
        resultado_esperado = [("SAMU", "193"), ("POLICIA", "190"), ("BOMBEIRO", "192")]
        # Chamada
        ressultado = phone.get_phonebook_reverse()
        # Avaliação
        assert ressultado == resultado_esperado

    def test_delete_succes(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Numero deletado"
        # Chamada
        resultado = phone.delete("POLICIA")
        # Avaliação
        assert resultado == resultado_esperado

    def test_delete_failure(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Não Encontrado Para Remoção"
        # Chamada
        resultado = phone.delete("POLICE")
        # Avaliação
        assert resultado == resultado_esperado

        """NOVOS TESTES IMPLEMENTADOS EM TDD"""

    def test_get_name_by_number(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "POLICIA"
        # Chamada
        resultado = phone.get_name_by_number("190")
        # Avaliação
        assert resultado == resultado_esperado

    def test_get_name_by_number_failed(self):
        # Setup
        phone = Phonebook()
        resultado_esperado = "Não Encontrado"
        # Chamada
        resultado = phone.get_name_by_number("180")
        # Avaliação
        assert resultado == resultado_esperado

    def test_change_number(self):
        # Setup
        phone = Phonebook()
        phone.add('SAMU', '190')
        expected_result = "Numero modificado"
        # Chamada
        result = phone.change_number("SAMU", "192")
        # Avaliação
        assert result == expected_result

