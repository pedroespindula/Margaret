#coding: utf-8

class Project:
	def __init__(self, name, description, mentor, aux_mentor, base_text, areas):
		self.name = name
		self.description = description
		self.base_text = base_text
		self.mentor = mentor
		self.aux_mentor = aux_mentor
		self.areas = areas
		self.state = "Em análise"
		self.subscribers = {}

	@property
	def areas(self):
		return self._areas
	
	@areas.setter
	def areas(self, areas):
		if not (areas in ['front', 'back', 'cloud', 'testes', 'documentação', 'refactoring', 'design', 'análise de dados', 'scrapping', 'automação', 'bot', 'devops']):
			raise Exception('Área Inválida')
		self._areas = areas

	@property
	def state(self):
		return self._state
		
	@state.setter
	def state(self, state):
		if not (state in ['Em análise', 'Necessita Revisão', 'Pronto - Com sugestões', 'Pronto - Completo']):
			raise Exception('Estado Inválido')
		self._state = state
		
	def add_subscriber(self, key, value):
		if key not in self.subscribers:
			self.subscribers[key] = value
		else:
			key += 1
			self.subscribers[key] = value
	
	def get_subscriber(self, key):
		return self.subscribers[key]
	
	def check_email(self, email):
		mentor = self.mentor
		if email == mentor["email"]:
			return True
		return False
