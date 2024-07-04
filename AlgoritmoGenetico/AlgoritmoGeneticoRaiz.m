


clc, clear all
F = @(x) (x.^2) - cos(3.*x);
n = 6;
%Generamos a las padres(con este haremos el primer torneo)
a = (10)*rand(1,n)-5;
Hijos =   Genetico(F,n,a);

Grafica = zeros(1,121);
Grafica(1) =F(Hijos(1));
%Con 120 iteraciones
for k=1:100
    Hijos = Genetico(F,n,Hijos);
    Grafica(k) = F(Hijos(1));

end    
Hijos

%Respuesta del algoritmo genetico
Hijos(1)
abs(F(Hijos(1)))
%Grafica del resultado de las generaciones 
plot(Grafica)





function [PintA] = Genetico(F,n,a)
    
    interval = [-5,5];
    %Aqui guardamos a los ganadores de los dos torneos realizados
    list1 = zeros(1,3);
    list2 = zeros(1,3);
    
    %Celula de las listas de ganadores
    Ganadores = {list1,list2};
    
    
  
    
    % Hacemos la seleción de padres
    %Torneo determinista 
    %Vamos generar 6 padres
    
    %Torneo de padres revuelto
    vector_revuelto = a(randperm(length(a)));
    
    
    %Celula de torneo
    Torneo = {a,vector_revuelto};
    
    
    for i = 1:2
        torneo = Torneo{i};
        ganad = Ganadores{i};
        for j =1:3
            
            if abs(F(torneo(2*j-1))) <  abs(F( torneo(2*j) ))
    
                ganad(j)=torneo(2*j-1);
    
            else
                ganad(j) = torneo(2*j);
    
            end
           
    
        end
    
        Ganadores{i} = ganad;
    
    end     
    
    %Lista de ganadores
    T1 = Ganadores{1};
    T2 = Ganadores{2};
    
    
    % Realizamos la cruza , para generar a los hijos
    % Generamos 6 hijos , mezclando los ganadores del torneo 1 con los del
    % torneo 2, 1-1.
    
    a1 = rand(1,1);
    Hijos = zeros(1,n);
    
    %Primeros 3 hijos
    for i= 1:3
        Hijos(i) = (1-a1)*T1(i) + a1*T2(i);
    end
    
    
    %Ahora invertimos a los torneos para generar otros tres hijos
    for i= 4:6
    
        Hijos(i) = (1-a1)*T2(i-3) + a1*T1(i-3);
    end
    
    
    %Hijos sin mutacion 
    
    
    % Hacemos la mutacion gausiana al azar, para todos los hijos
    %1 si mutamos al hijo 0 no lo mutamos
    
    %Haremos una determinada cantidad de mutaciones a los hijos
    
    for k = 1:n
        Mutacion = randi([0,1]);
        
        
        if Mutacion == 0
            Mn = randn(1,1);
            Hijos(k) = Hijos(k) + Mn;
        end    
    
    end 
    
    %Hijos con mutaciones
    Hijos;

    %Ahora realizamos la generacion1 juntando a los padres y los hijos
    %mutados , escogiendo a los mejores 6

    Pint = zeros(1,12);
    PintA = zeros(1,6);
    Aux = [a,Hijos];
    

    Aux ;
    for l = 1:12 
        Pint(l) = abs(F(Aux(l)));
    end    
    Pint;
    [~,Aux2] = sort(Pint);
    

    for i= 1:6

        PintA(i) = Aux( Aux2(i)  );
    end    
    Aux2;
    PintA;
    
    



end 