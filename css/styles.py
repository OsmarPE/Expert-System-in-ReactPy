from reactpy import html


def getStyles():
    return html.style("""
    *{
        margin: 0;
        box-sizing:border-box;
        font-family:'Outfit'
    }
                   
    body #app{
        background-image:linear-gradient(180deg, #F3E5D0 0% , #fff 100% );
        height:100vh;
        display:flex;
        align-items:center;
        justify-content:center;
                      
    }
                   
    input,select{
        appearance: none; /* Hide default appearance */
        -webkit-appearance: none; /* For Safari */
        -moz-appearance: none; /* For Firefox */
        cursor:pointer;
        outline:0;
        width:100%;
        height:44px;
        padding:0 .5rem;
        background-color:#F3EBE1;
        border:2px solid rgba(0,0,0,0.5);
        border-radius:0.25rem;
        font-size:0.875rem;
    }
                      
 
   
""")