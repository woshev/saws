﻿// Автор: Зубов Н.С.
program n_1;
var i,k,max:integer;
begin
   k:=0;
   max:=0;
   for i:= 1156 to 12209 do begin
       if ((i mod 2 = 0)or(i mod 5=0)) and ((i mod 7 <> 0) and (i mod 13<> 0) and (i mod 17 <> 0) and (i mod 23 <> 0)) then begin
       inc(k);
       max:=i;
       end;
   end;
   writeln(k,' ',max);
end.