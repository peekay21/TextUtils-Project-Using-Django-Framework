# This file is created by Pradip Kumar Murmu

from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
     
     return render(request, 'index2.html')

def ex1(request):
     return HttpResponse(
          '''
          <h1> Harry bhai challenge accepted </h1>
          <ul>
          <li> <a href='https://www.youtube.com'>YouTube</a></li>
          <li> <a href='https://www.google.com'>Google here</a></li>
          <li> <a href='https://www.github.com'>Github</a></li>
          <li> <a href='https://www.linkedln.com'>Linkedin</a></li>
          </ul>
          '''
     )


def analyze(request):
     djtext = request.GET.get('text','default')
     removepun = request.GET.get('removepunc', 'off')
     fullcaps = request.GET.get('fullcaps', 'off')
     newlineremover = request.GET.get('newlineremover', 'off')
     charcount= request.GET.get('charcount', 'off')
     extraspaceremover= request.GET.get('extraspaceremover', 'off')
     if removepun == 'on':

          punctuations ='''~`!@#$%^&*()_+-={[]}|:;"'<,.>/'''
          analyzed = ''
          for char in djtext:
               if char not in punctuations:
                    analyzed +=char
          params = {   
               'purpose' : 'Removed Punctuations',
               'analyzed_text':analyzed,
          }
          return render(request, 'analyze2.html', params)


     elif fullcaps =='on':

          analyzed =''
          for char in djtext:
               analyzed += char.upper()
          params ={
               'purpose': 'Text to UPPER CASE',
               'analyzed_text':analyzed
          }
          return render(request, 'analyze2.html', params)
     elif newlineremover =='on':
          analyzed = ''

          for char in djtext:
               if char != '\n':
                    analyzed += char
          params ={
               'purpose':' New Line remover',
               'analyzed_text' : analyzed
          }

          return render(request, 'analyze2.html', params)

     elif extraspaceremover =='on':
          analyzed = ''

          count1 = 0
          for char in djtext:
               if char==' ':
                    count1 +=1
               if count1 >1:
                    count1 -=1
                    continue
               if char!=' ' or count1 <=1:
                    analyzed += char
                    count1 =0
                    


          params ={
               'purpose' : '',
               'analyzed_text' : analyzed
          }
          return render(request, 'analyze2.html', params)


     else:
          return render(request, 'index2.html')


# def capitalizefirst(request):
#      return HttpResponse('capitalize first')


# def newlineremove(request):
#      return HttpResponse(' NEW Line remove')

# def charcount(request):
#      return HttpResponse('Char count')

# def spaceremove(request):
#      return HttpResponse('space remove')
          