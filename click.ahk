^SPACE::  Winset, Alwaysontop, , A
return

^+SPACE::  Winset, Alwaysontop, off , A
return

#IfWinActive MTGA
+Space::
Click
return

#IfWinActive MTGA
+,::
Click Down
return

#IfWinActive MTGA
+.::
Click Up
return
