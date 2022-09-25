from django.http import HttpResponse

def str1(request):
    return HttpResponse("<p>Привет, меня зовут Тюпин Даниил. Я из Москвы.<p>"
                        "<p>Благодаря Яндекс Лицею я имею 2 года опыта программмирования на Python.<p>"
                        "<p>Помимо программирования я увлекаюсь кулинарией, чтением и книг и спортом<p>"
                        '<div>'
                        '<img src="https://raw.githubusercontent.com/Vuuk3/Project/main/1664117970700.jpg" '
                        'width="300" height="300">'
                        '</div>')