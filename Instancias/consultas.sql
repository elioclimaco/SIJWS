/*
 Obtiene todas las instancias de acuerdo a una Sede
 y Distrito Judicial.
 */
Select I.c_distrito, D.x_nom_distrito, I.c_sede, S.x_desc_sede, I.c_instancia, I.x_nom_instancia from instancia as I
Inner join sede as S on I.c_sede = S.c_sede
Inner join distrito_judicial as D on I.c_distrito = D.c_distrito
ORDER BY I.c_distrito, S.c_sede, I.c_instancia