%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  rutas.pl
%  Ejemplo de una base de conocimiento en Prolog para encontrar la mejor ruta 
%  entre estaciones de un sistema de transporte masivo.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Hechos: conexion/3  %%
%%%%%%%%%%%%%%%%%%%%%%%%%%
% conexion(Estacion1, Estacion2, Costo).

conexion(a, b, 5).
conexion(b, c, 2).
conexion(c, d, 10).
conexion(a, e, 3).
conexion(e, f, 2).
conexion(f, d, 3).
conexion(c, e, 1).
conexion(b, f, 4).
conexion(d, g, 2).
conexion(e, g, 5).

:- discontiguous conexion/3.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  Rules for finding the best route between stations
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Base case: direct connection
ruta(X, Y, [X, Y], C) :-
    conexion(X, Y, C).

% Recursive case: route through intermediate stations
ruta(X, Y, [X|Camino], CostoTotal) :-
    conexion(X, Z, Costo1),
    ruta(Z, Y, Camino, Costo2),
    CostoTotal is Costo1 + Costo2.

% Find the best route
mejor_ruta(X, Y, MejorCamino, MejorCosto) :-
    setof((Ruta, Costo),
          ruta(X, Y, Ruta, Costo),
          Conjunto),
    seleccionar_mejor(Conjunto, (MejorCamino, MejorCosto)).

% Select the best route from a set
seleccionar_mejor([(R, C)], (R, C)).
seleccionar_mejor([(R, C)|T], (Rm, Cm)) :-
    seleccionar_mejor(T, (R2, C2)),
    ( C < C2 ->
        Rm = R,
        Cm = C
    ;
        Rm = R2,
        Cm = C2
    ).
