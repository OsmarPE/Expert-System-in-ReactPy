from reactpy import component,html,use_state,use_effect
from fastapi import FastAPI
import reactpy
from reactpy.backend.fastapi import configure
from components.Header import Header
from helpers.api import readJSON
from helpers.utils import filterBooks
from components.Book import Book
from components.Form import Form
from components.Modal import Modal
from css.styles import getStyles

# configurate of styles and scrips

css = html.link({'rel':'stylesheet','href':'https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap'})
tailwind = html.script({'src':'https://cdn.tailwindcss.com'})
remix = html.link({'href':'https://cdn.jsdelivr.net/npm/remixicon@3.5.0/fonts/remixicon.css','rel':'stylesheet'})
reset = getStyles()

attrMain = {
    "style":{
        "fontFamily":'Outfit'
    },
    "class":"max-w-[480px] w-[90%] mx-auto p-7 bg-[#F8F3ED] shadow-[6px_16px_40px_0_rgba(0,0,0,0.08)] rounded-lg"
}



# main component
@component
def Main():
    
    book , setBook = use_state({
        'titulo':'',
        'img':'',
        'descripcion':'',
    })
    modalShow, setModalShow = use_state(False)
    typeBook,setTypeBook = use_state({
            'edad':'',
            'motivo':'',
            'tiempo':'',
            'cantidad':'',
    })
  

    async def getDatos():
        # if empty properties of typeBook:
        if typeBook['edad'] and typeBook['motivo'] and typeBook['tiempo'] and typeBook['cantidad']:
            # get data json
            datos = await readJSON('data.json')
            # filter books 
            book = filterBooks(datos,typeBook['edad'],typeBook['cantidad'],typeBook['motivo'] ,typeBook['tiempo']  )
           
            if len(book):
                # print book find
                setBook({
                    'titulo':book[0]['Respuesta'],
                    'img':book[0]['Imagen'],
                    'descripcion':book[0]['Descripcion']
                })

                # show modal with book find
                setModalShow( not modalShow)
                return
            

    # getDatos dependicies the typebook
    use_effect( getDatos,dependencies=[typeBook] )

    return html.main(
        attrMain,
        tailwind,
        remix,
        reset,
        css,
        Modal(modalShow, setModalShow,book),
        Header('BOOKS'),
        Form(setTypeBook,setModalShow,modalShow),
    )


# initialization project
app = FastAPI()
configure(app,Main)

