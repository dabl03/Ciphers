TEST=False;#If is true, test(), else main();
"""
     Programa que cifra usando el cifrado M4X1
    Funciones disponibles:
    is_str_and_not_void : Comprueba que el paratmetro sea una cadena y que no este vacia.
    cifrar : Cifra. Si no entiendes como sifra: Consiste en trasladar las letras tres lugares hacia atrás. (M4X1)[https://gravityfalls.fandom.com/es/wiki/Lista_de_Criptogramas#:~:text=Tabla%20de%20Cifrado-,Tabla%20de%20Cifrado%20%22M4X1%22,Consiste%20en%20trasladar%20las%20letras%20tres%20lugares%20hacia%20atr%C3%A1s.,-Criptograma]
    des_cifrar : descifra.
"""
def is_str_and_not_void(str_=""):
    return type(str_)==str and len(str_)>0;
def cifrar(normal) -> str:
    cifrado="";
    if not is_str_and_not_void(normal):
        return None;
    for char in normal:
        n_char=ord(char);
        #Comprobación
        if not char.isalpha():
            cifrado+=char;
            #char>"b":
        elif ord(char.lower())>ord('c'):
            #Retrocedemos 3 caracteres.
            cifrado+='%c'%(n_char-3);
        else:
            #a: x, b: y, c: z
            if n_char>90:
                na=ord('a');
                nz=ord('z');
            else:
                na=ord('A');
                nz=ord('Z');
            #   z-(if a:2, b:1, c:0)
            out="%c"%(nz-(2-(n_char-na)))
            cifrado+=out;
    return cifrado;

def des_cifrar(cifrado=""):
    d_cifrado="";
    if not is_str_and_not_void(cifrado):
        return None;
    for char in cifrado:
        if not char.isalpha():
            d_cifrado+=char;
        elif ord(char.lower())<ord('x'):
            d_cifrado+='%c'%(ord(char)+3);
        else:
            au=ord(char.lower())-ord('x');
            d_cifrado+='%c'%((ord('a') if char.islower() else ord('A'))+au);
    return d_cifrado;

def test(show=False):
    import time;
    abc=''.join( ("%c"%c for c in range(ord('a'),ord('z')+1)) );
    c_abc="xyzabcdefghijklmnopqrstuvw";
    if not (cifrar("")==None and cifrar(123)==None):
        print("ERROR: No se comprueba el tipo de dato. en la funcion cifrar");
        return -1;
    normal=("hola mundo","Como estas?","como te llamas", "yo daniel","buenos dias");
    print("\n---------------------------------------");
    print("Prueba de la funcion cifrar:")
    n_times={};
    for i in range(1000):
        t_a=time.time();
        cifrado=[cifrar(str_) for str_ in normal];
        time.sleep(0.01);
        t=time.time()-t_a;
        if t in n_times:
            n_times[t]+=1;
        else:
            n_times[t]=1;
    if show:
        for i in range(len(normal)):
            print("\n    - Normal: {}\n    - Cifrado: {}".format(normal[i],cifrado[i]) );
    print();
    print("- Time: ",n_times);
    if not cifrar(abc)==c_abc:
        print("hay un error en la funcion cifrar:");
        print("   normal: "+abc+"\n   cifrado: "+cifrar(abc)+"\n   como deberia ser: "+c_abc);
    
    print("\n---------------------------------------");
    if not (des_cifrar("")==None and des_cifrar(123)==None):
        print("ERROR: No se comprueba el tipo de dato. en la funcion des_cifrar");
        return -1;
    print("\nPrueba de la funcion des_cifrar:");
    n_times={};
    for i in range(1000):
        t_a=time.time();
        normal=[des_cifrar(str_) for str_ in cifrado];
        time.sleep(0.01);
        t=time.time()-t_a;
        if t in n_times:
            n_times[t]+=1;
        else:
            n_times[t]=1;
    if show:
        for i in range(len(normal)):
            print("\n    - Cifrado:{}\n     - Normal: {}".format(cifrado[i],normal[i]) );
    print();
    print("- Time: ",n_times);
    if not des_cifrar(c_abc)==abc:
        print("hay un error en la funcion des_cifrar:");
        print("   cifrado: "+c_abc+"\n   descifrado: "+des_cifrar(c_abc)+"\n   como deberia ser: "+abc);
    print("\n---------------------------------------");

def main():
    help_="1- Para cifrar, 2- Para cifrar continuo. 3- Para descifrar. 4- Descifrar continuo. 9-Help. 0- para salir o quit.";
    h="{}:\n    quit- para salir o 0- para salir, help: esta ayuda.";
    def input_interprete(name,func,out_of_input=" <<< ",out_of_out=" >>> "):
        print(h.format(name));
        while True:
            io=input(out_of_input);
            out=func(io);
            print(out_of_out+str(out));
            print();
            io=io.lower();
            if io=="0" or io=="quit":
                break;
            elif io=="help":
                print(h.format(mame));
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
                input_interprete("Cifrado continuo:",cifrar," <<< "," >>> ");
                continue;
            elif io==3:
                print("Descifrar:");
                io=input(" <-- ");
                out=des_cifrar(io);
                print(" --> "+str(out));
            elif io==4:
                input_interprete("Descifrado continuo:",des_cifrar," <--- "," ---> ");
            elif io==9:
                print(help_);
            elif io==0:
                break;
            continue;
        elif io=="quit":
            break;
        print("No se reconoce el comando:(");
if __name__ == '__main__':
    if TEST:
        test(True);
    else:
        main();