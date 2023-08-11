from reactpy import component, html

attrModal = {
    "class":"absolute inset-0  bg-[rgba(255,255,255,0.20)] flex items-center justify-center",
    "style":{"backdropFilter": "blur(8px)",}
}
attrModalMain = {
    "class":"w-[90%] max-w-[500px] bg-white rounded-lg overflow-hidden shadow-[0px_4px_20px_0px_rgba(0,0,0,0.04)] ",
    
}

@component
def Modal(modalShow, setModalShow,book):
    return html.div(
        {
            "on_click": lambda e: setModalShow( not modalShow),
            "class":"absolute backdrop-blur inset-0  bg-[rgba(0,0,0,0.1)] flex items-center justify-center",
            "style":{'transition':'all 0.4s 0.1s ease','opacity':f'{ "1" if modalShow else "0"}','pointer-events':f'{ "initial" if modalShow else "none"}'}
        },
        html.main(
            {"class":"w-[90%] max-w-[500px] bg-white rounded-lg overflow-hidden shadow-[0px_4px_20px_0px_rgba(0,0,0,0.02)]",
             "style":{'transition':'all 0.4s ease','transform':f'translateY({ "0" if modalShow else "-14%"} )','opacity':f'{"1" if modalShow else "0"} '}
             },
            html.div(
                {'class':'p-6 bg-[#F8F3ED] relative'},
                html.button(
                    {'class':'absolute top-4 right-4',"on_click":lambda e: setModalShow( not modalShow ) },
                    html.i({'class':'ri-close-line text-2xl '}),
                ),
                html.h2({'class':'text-center text-2xl font-semibold mb-4 py-2'},book["titulo"]),
                html.img({
                    'src':'https://lienzolibreria.com/cdn/shop/products/untitled-project-63bcff773c241e7ff0cf6208_2x_a8969ee0-9662-4c21-916c-09038160866f.webp?v=1673331201&width=713',
                    'class':' block object-cover w-[16rem] mx-auto'
                    })
            ),
            html.div(
                {'class':'py-6 px-9 text-center bg-white capitalize'},
                html.p({book["descripcion"]})
            )
        )
    )

