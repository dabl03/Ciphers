normal=("hola mundo","Como estas?","como te llamas", "yo daniel","buenos dias");
abc=''.join( ("%c"%c for c in range(ord('a'),ord('z')+1)) );
TEST=False;#If is true, test(), else main();
version="""
    Copyright (c) 2023 Daniel Alexander - dabl03@outlook.com
    Version: V1.0.0
"""
def is_str_and_not_void(str_="")->bool:
	### Comprueba si es una cadena o sino esta vacía.
    return type(str_)==str and len(str_)>0;
def title_show(str_,width):
    print('|'+('-'*width)+'|');
    print('|'+(
        (' '*int( (width/2)-len(str_)/2) )+str_+(' '*int((width/2)-len(str_)/2))
    )+'|');
    print('|'+('-'*width)+'|');

def input_interprete(name,func,help_,out_of_input=" <<< ",out_of_out=" >>> "):
    print(help_.format(name));
    while True:
        io=input(out_of_input);
        out=func(io);
        print(out_of_out+str(out));
        print();
        io=io.lower();
        if io=="0" or io=="quit":
            break;
        elif io=="help":
            print(help_.format(mame));

def cifrar(str_)->bool:
    cifrado="";
    return False;
def des_cifrar(str_)->bool:
    if not is_str_and_not_void(str_):
        return True;
    return False;
def test(c_abc,name,func,normal,show,abc=None)->int:
    import time;
    if abc==None: abc=''.join( ("%c"%c for c in range(ord('a'),ord('z')+1)) );
    if not (func("")==None and func(123)==None):
        print("ERROR: No se comprueba el tipo de dato. En la función {}.".format(name));
        return -1;
    print("\n---------------------------------------");
    print("Prueba de la funcion {}:".format(name))
    n_times={};
    for i in range(1000):
        t_a=time.time();
        cifrado=[func(str_) for str_ in normal];
        time.sleep(0.01);
        t=time.time()-t_a;
        if t in n_times:
            n_times[t]+=1;
        else:
            n_times[t]=1;
    if show:
        for i in range(len(normal)):
            print("\n    - Antes: {}\n    - Después: {}".format(normal[i],cifrado[i]) );
    print();
    print("- Time: ",n_times);
    if not func(abc)==c_abc:
        print("hay un error en la función: {}".format(name));
        print("   normal: {}\n   cifrado: {}\n   como debería ser: {}".format(abc,func(abc),c_abc));
        return -1;
    
    print("\n---------------------------------------");
    return 0;
def main(cls_this):
    title_show("Cipher "+cls_this.name,cls_this.width);
    cifrar=cls_this.cifrar;
    des_cifrar=cls_this.des_cifrar;
    help_=version+"\n1- Para cifrar, 2- Para cifrar continuo. 3- Para descifrar. 4- Descifrar continuo. 9-Help o help. 0- para salir o quit.";
    h="{}:\n    quit- para salir o 0- para salir, help: esta ayuda.";
    print(help_);
    while True:
        io=input("> ");
        if io.isnumeric():
            io=int(io);
            if io==1:
                print("Cifrar:")
                io=input(" << ");
                out=cifrar(io);
                print(" >> "+str(out));
                continue;
            elif io==2:
                input_interprete("Cifrado continuo:",cifrar,h," <<< "," >>> ");
                continue;
            elif io==3:
                print("Descifrar:");
                io=input(" <-- ");
                out=des_cifrar(io);
                print(" --> "+str(out));
            elif io==4:
                input_interprete("Descifrado continuo:",des_cifrar,h," <--- "," ---> ");
            elif io==9:
                print(help_);
            elif io==0:
                break;
            continue;
        elif io=="quit":
            break;
        elif io=="help":
            print(help_);
            continue;
        print("No se reconoce el comando:(");

def tratar_arg(argv):
    mode=[]
    for arg in argv:
        if arg[0]=='-' and len(arg)>1 and arg[1]=='-':
            if arg[2:]=='v' or arg[2:]=="version":
                print(version);
            elif arg[2:]=='t' or arg[2:]=="tester":
                mode.append("tester");
            elif arg[2:]=='h' or arg[2:]=="help":
                print(version+"""\nPor ahora estos son los argumentos disponibles:
                        --v o --version : Muestra la versión y la licencia usada en esta App.
                        --t o tester : Activa el modo testeo de esta App.
                        --h o help : Muestra este menú de ayuda.""");
    return mode;