"""programa para manipular archivos"""
import os
import json

def create_file(file_name:str, content:(list , dict, str) = None)-> None:
    
    """crear un archivo con contenido o sin contenido"""
   
    mode = "w" if content else "x"
    try:
        file=open(file_name,mode)
    except FileExistsError as error:
        raise OSError(f"El archivo'{file_name}' ya  existe") from error
    
    except PermissionError as error:
        raise OSError(f"NO tienes permiso de crear el archivo '{file_name}'") from error
   
    """if content:
       mode ="w" todo este if else es igual a la linea 5
    #else:
    #   mode = "x"
    #file=open(file_name,mode)"""
    

    if content:
        if isinstance(content,(dict,list)): 
            content = json.dumps(content)
        file.write(content)          
    file.close
    
    
def update_file(file_name: str, content:(list,dict,str) ) -> None:
   
    """Modifica el archivo file_name
    Si overwite es verdadero, sobreescribe el archivo"""
    
    if not isinstance(content, (dict,list)) or content == "":
        raise ValueError(f"'{content}' argument must be specified")
   
    if not os.path.exists(file_name):
         raise FileNotFoundError(f"File '{file_name}' was not found") from error
     
    file = open(file_name)
    file_content=json.loads(file.read())
    file.close()
    
    
    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)
        elif isinstance(content, list):
            file_content +=content
            
    elif  isinstance(file_content, dict):
        if isinstance(content,dict):
            #file_content =file_content | content
            file_content=[file_content,content]
        elif isinstance(contet,list):  
            file_content=[file_content + content ] 
            
        
    file=open(file_name,"w")   
    file.write(json.dumps(file_content))
    file.close()

def read_file(file_name)->str:
    #file=open(file_name,"r") esta esta bien pero si no se pone nada en
    #                         la forma de abrir el arch por defal es read
    if not os.path.exists(file_name):
        raise FileNotFoundError(f'File {file_name} was not found')
    print(file_name)
    file = open(file_name)
    content = json.loads(file.read())
    file.close()
    return content