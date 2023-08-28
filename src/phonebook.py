class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nome invalido'  # Bug resolvido para retornar 'Nome invalido'.
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'  # Bug resolvido para retornar 'Nome invalido'.
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'

        if len(number) == 0:  # Refactoring: Uma string pode ser igual a 0 mas nunca menor que 0
            return 'Numero invalido'  # Bug resolvido para retornar 'Nome invalido'

        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'  # Bug de identação resolvido
        else:
            return "Esse Nome Ja foi adicionado"  # Refactoring: Implementado um else para retorno negativo

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if '#' in name:
            return 'Nome invaldo'
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nome invalido'  # Bug resolvido para retornar 'Nome invalido'
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome invalido'  # Bug resolvido para retornar 'Nome invalido'
        # Refactoring: Implementado o metodo com uma busca antes do retorno para um retorno positivo e negativo
        for achou in self.entries:
            if achou == name:
                return self.entries[name]
            else:
                return "Nome Não Encontrado"

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())  # Refactoring: Convertendo dicionario em lista para retornar a chave

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())  # Refactoring: Convertendo dicionario em lista para retornar o valor

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name, number})
                return result
            else:  # Refactoring: else para um reotno negativo
                return "Name not found"

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries.items())  # Refactoring: Usando a função sorted() para retornar uma lista ordenada

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return sorted(self.entries.items(),
                      reverse=True)  # Refactoring: Usando a função sorted() com o reserve=True para retornar uma lista em ordem inversa.

    def delete(self, search_name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        # Refactoring: Implementado o metodo com uma busca antes da remoção para que seja dado um retorno positivo e negativo
        for achou in self.entries:
            if achou == search_name:
                self.entries.pop(search_name)
                return "Numero deletado"
        return "Não Encontrado Para Remoção"

    """NOVOS METODOS IMPLEMENTADOS EM TDD"""

    def get_name_by_number(self, number):
        for entry_name, entry_number in self.entries.items():
            if entry_number == number:
                return entry_name
        return "Não Encontrado"

    def change_number(self, name, new_number):
        for entry_name, entry_number in self.entries.items():
            if entry_name == name:
                self.entries[name] = new_number
                return "Numero modificado"
        return "Número nao modificado"
