﻿// Автор: Зубов Н.С.
program n_1;
var i,k,min:integer;
begin
   k:=0;
   min:=9999999;
   for i:= 1045 to 8963 do begin
       if ((i mod 5 = 0)or(i mod 7=0)) and ((i mod 13 <> 0) and (i mod 11<> 0) and (i mod 17 <> 0) and (i mod 19 <> 0)) then begin
       inc(k);
       if min>i then min:=i;
       end;
   end;
   writeln(k,' ',min);
end.