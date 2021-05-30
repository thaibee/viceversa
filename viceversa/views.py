from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html')


def reverse(requests):
    text = requests.GET['text_to_reverse']
    len_text = len(text.split())
    rev_text = text[::-1]
    return render(requests, 'reversed.html', {
        'text': text,
        'len_text': len_text,
        'rev_text': rev_text
    })
