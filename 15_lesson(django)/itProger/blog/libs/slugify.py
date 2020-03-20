# Импортируем slugify
from django.template.defaultfilters import slugify as django_slugify

# Создаем словарь, чтобы преобразовывать кириллицу в латиницу
alphabet = {'а': 'a','б': 'b','в': 'v','г': 'g','д': 'd','е': 'e','ё': 'yo','ж': 'zh','з': 'z','и': 'i', 'й': 'j','к': 'k','л': 'l','м': 'm','н': 'n','о': 'o','п': 'p','р': 'r','с': 's','т': 't', 'у': 'u','ф': 'f','х': 'kh','ц': 'ts','ч': 'ch','ш': 'sh','щ': 'shch','ы': 'i','э': 'e','ю': 'yu', 'я': 'ya'}

# Создаем функцию, что переводит текст из латиницы в кириллицу
def slugify(s):
	# Возвращаем вызов slugify, где перебираем все символы в строке «s» и переводим их в латиницу
	return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))

# теперь текст будет переводиться в формат подходящий для ссылок
# Пример: «было так» > «stalo-tak»