
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRE_CH ABRE_CLT ABRE_P ASPAS AUX BOOLEANO COMENT COMPILADORES DEFINE DELIMITADOR DOIS_PONTOS ENQUANTO ESCREVA FECHA_CH FECHA_CLT FECHA_P FIM IFSULDEMINAS INICIO INTERROMPA LEIA NUMERO_MF OP_ARIT OP_ATRIBUI OP_LOGICO OP_REL PARA SE SENAO TEXTO_MF VALOR_NUMDEC VALOR_NUMINT VALOR_TEXTO VAR VARIAVEL_MF VIRGULA ignore\n    statements : statements statement\n    \n    statements : statement\n    \n    statement : COMENT\n    \n    statement : INTERROMPA DELIMITADOR\n\n    \n    statement : IFSULDEMINAS DELIMITADOR\n    \n    statement : COMPILADORES DELIMITADOR\n    \n    statement : INICIO ABRE_CH FECHA_CH\n    \n    statement : FIM ABRE_CH FECHA_CH\n    \n    statement : DEFINE ABRE_P VAR FECHA_P ABRE_CLT statement FECHA_CLT\n              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P FECHA_CLT FECHA_CLT\n              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT FECHA_CLT\n              | DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT SENAO ABRE_CLT statement FECHA_CLT FECHA_CLT \n              \n    \n    statement : ENQUANTO ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT\n              \n    \n    statement : PARA ABRE_P VAR OP_ATRIBUI VALOR_NUMINT VIRGULA cond_param VIRGULA VAR OP_ARIT OP_ARIT FECHA_P ABRE_CLT statements FECHA_CLT\n    \n    statement : VAR OP_ATRIBUI VALOR_NUMINT DELIMITADOR\n             | VAR OP_ATRIBUI VALOR_NUMDEC DELIMITADOR\n             | VAR OP_ATRIBUI VALOR_TEXTO DELIMITADOR\n             | VAR OP_ATRIBUI VAR OP_ARIT OP_ARIT DELIMITADOR\n             | VAR OP_ATRIBUI VAR DELIMITADOR\n             | VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMINT DELIMITADOR\n             | VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMDEC DELIMITADOR\n             | VAR OP_ATRIBUI funcao DELIMITADOR\n             | VAR DELIMITADOR\n             | VAR OP_ATRIBUI VAR OP_ARIT VAR DELIMITADOR\n    \n    statement : SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT\n              | SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT SENAO ABRE_CLT statements FECHA_CLT\n            \n    \n    statement : funcao DELIMITADOR\n    \n    statement : funcao ABRE_CLT statements FECHA_CLT\n    \n    cond_param : VAR OP_REL VALOR_NUMINT\n              | VAR OP_REL VALOR_NUMDEC\n              | VAR OP_REL VALOR_TEXTO\n\n              | VAR OP_REL VALOR_NUMINT OP_LOGICO VAR OP_REL VALOR_NUMINT\n              | VAR OP_REL VALOR_NUMDEC OP_LOGICO VAR OP_REL VALOR_NUMDEC\n              | VAR OP_REL VALOR_TEXTO OP_LOGICO VAR OP_REL VALOR_TEXTO\n              | BOOLEANO\n    statement : AUX\n    statement : ESCREVA ABRE_P VAR FECHA_P DELIMITADOR\n              | ESCREVA ABRE_P ASPAS statements ASPAS FECHA_P DELIMITADOR\n              | ESCREVA ABRE_P param FECHA_P DELIMITADOR\n              | ESCREVA ABRE_P param DOIS_PONTOS\n    statement : BOOLEANO\n                    \n    statement : LEIA ABRE_P VAR FECHA_P DELIMITADOR\n\n    \n    cond_param : cond_param OP_REL cond_param\n    \n    param_vazio :\n    \n    param : VALOR_NUMINT\n          | VALOR_NUMDEC\n          | VALOR_TEXTO\n          | VAR\n    \n    param : param VIRGULA param\n    \n    funcao : ABRE_P param_vazio FECHA_P\n          | ABRE_P param FECHA_P\n    '
    
_lr_action_items = {'COMENT':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[3,3,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,3,-7,-8,3,3,-19,-15,-16,-17,-22,-28,3,-40,3,3,3,-37,-39,-42,-24,-18,-20,-21,3,3,-9,-25,-13,-38,3,3,3,-10,-26,-11,3,3,3,-14,-12,]),'INTERROMPA':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[4,4,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,4,-7,-8,4,4,-19,-15,-16,-17,-22,-28,4,-40,4,4,4,-37,-39,-42,-24,-18,-20,-21,4,4,-9,-25,-13,-38,4,4,4,-10,-26,-11,4,4,4,-14,-12,]),'IFSULDEMINAS':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[5,5,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,5,-7,-8,5,5,-19,-15,-16,-17,-22,-28,5,-40,5,5,5,-37,-39,-42,-24,-18,-20,-21,5,5,-9,-25,-13,-38,5,5,5,-10,-26,-11,5,5,5,-14,-12,]),'COMPILADORES':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[6,6,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,6,-7,-8,6,6,-19,-15,-16,-17,-22,-28,6,-40,6,6,6,-37,-39,-42,-24,-18,-20,-21,6,6,-9,-25,-13,-38,6,6,6,-10,-26,-11,6,6,6,-14,-12,]),'INICIO':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[7,7,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,7,-7,-8,7,7,-19,-15,-16,-17,-22,-28,7,-40,7,7,7,-37,-39,-42,-24,-18,-20,-21,7,7,-9,-25,-13,-38,7,7,7,-10,-26,-11,7,7,7,-14,-12,]),'FIM':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[8,8,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,8,-7,-8,8,8,-19,-15,-16,-17,-22,-28,8,-40,8,8,8,-37,-39,-42,-24,-18,-20,-21,8,8,-9,-25,-13,-38,8,8,8,-10,-26,-11,8,8,8,-14,-12,]),'DEFINE':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[9,9,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,9,-7,-8,9,9,-19,-15,-16,-17,-22,-28,9,-40,9,9,9,-37,-39,-42,-24,-18,-20,-21,9,9,-9,-25,-13,-38,9,9,9,-10,-26,-11,9,9,9,-14,-12,]),'ENQUANTO':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[13,13,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,13,-7,-8,13,13,-19,-15,-16,-17,-22,-28,13,-40,13,13,13,-37,-39,-42,-24,-18,-20,-21,13,13,-9,-25,-13,-38,13,13,13,-10,-26,-11,13,13,13,-14,-12,]),'PARA':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[14,14,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,14,-7,-8,14,14,-19,-15,-16,-17,-22,-28,14,-40,14,14,14,-37,-39,-42,-24,-18,-20,-21,14,14,-9,-25,-13,-38,14,14,14,-10,-26,-11,14,14,14,-14,-12,]),'VAR':([0,1,2,3,10,16,18,20,21,22,23,26,33,34,35,36,37,38,39,40,41,42,43,47,58,60,65,66,67,68,69,70,72,76,78,80,82,87,92,94,96,97,100,101,102,103,104,105,106,107,108,109,111,112,113,117,119,125,126,127,134,136,138,140,143,144,146,148,149,],[11,11,-2,-3,32,-36,-41,-1,-4,-5,-6,44,48,-23,54,54,57,-27,11,59,62,-7,-8,32,11,11,83,-19,-15,-16,-17,-22,54,-28,11,-40,11,11,11,-37,-39,-42,-24,-18,-20,-21,11,114,115,116,11,54,-9,54,-25,-13,-38,131,11,11,11,-10,-26,-11,11,11,11,-14,-12,]),'SE':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[12,12,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,12,-7,-8,12,12,-19,-15,-16,-17,-22,-28,12,-40,99,12,12,-37,-39,-42,-24,-18,-20,-21,12,12,-9,-25,-13,-38,12,12,12,-10,-26,-11,12,12,12,-14,-12,]),'AUX':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[16,16,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,16,-7,-8,16,16,-19,-15,-16,-17,-22,-28,16,-40,16,16,16,-37,-39,-42,-24,-18,-20,-21,16,16,-9,-25,-13,-38,16,16,16,-10,-26,-11,16,16,16,-14,-12,]),'ESCREVA':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[17,17,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,17,-7,-8,17,17,-19,-15,-16,-17,-22,-28,17,-40,17,17,17,-37,-39,-42,-24,-18,-20,-21,17,17,-9,-25,-13,-38,17,17,17,-10,-26,-11,17,17,17,-14,-12,]),'BOOLEANO':([0,1,2,3,16,18,20,21,22,23,34,35,36,38,39,42,43,58,60,66,67,68,69,70,72,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,109,111,112,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[18,18,-2,-3,-36,-41,-1,-4,-5,-6,-23,55,55,-27,18,-7,-8,18,18,-19,-15,-16,-17,-22,55,-28,18,-40,18,18,18,-37,-39,-42,-24,-18,-20,-21,18,18,55,-9,55,-25,-13,-38,18,18,18,-10,-26,-11,18,18,18,-14,-12,]),'LEIA':([0,1,2,3,16,18,20,21,22,23,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[19,19,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,19,-7,-8,19,19,-19,-15,-16,-17,-22,-28,19,-40,19,19,19,-37,-39,-42,-24,-18,-20,-21,19,19,-9,-25,-13,-38,19,19,19,-10,-26,-11,19,19,19,-14,-12,]),'ABRE_P':([0,1,2,3,9,12,13,14,16,17,18,19,20,21,22,23,33,34,38,39,42,43,58,60,66,67,68,69,70,76,78,80,82,87,92,94,96,97,99,100,101,102,103,104,108,111,113,117,119,126,127,134,136,138,140,143,144,146,148,149,],[10,10,-2,-3,26,35,36,37,-36,40,-41,41,-1,-4,-5,-6,10,-23,-27,10,-7,-8,10,10,-19,-15,-16,-17,-22,-28,10,-40,10,10,10,-37,-39,-42,112,-24,-18,-20,-21,10,10,-9,-25,-13,-38,10,10,10,-10,-26,-11,10,10,10,-14,-12,]),'$end':([1,2,3,16,18,20,21,22,23,34,38,42,43,66,67,68,69,70,76,80,94,96,97,100,101,102,103,111,113,117,119,136,138,140,148,149,],[0,-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,-7,-8,-19,-15,-16,-17,-22,-28,-40,-37,-39,-42,-24,-18,-20,-21,-9,-25,-13,-38,-10,-26,-11,-14,-12,]),'FECHA_CLT':([2,3,16,18,20,21,22,23,34,38,42,43,58,66,67,68,69,70,76,80,94,96,97,98,100,101,102,103,104,108,111,113,117,119,126,132,133,134,136,137,138,140,145,146,147,148,149,],[-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,-7,-8,76,-19,-15,-16,-17,-22,-28,-40,-37,-39,-42,111,-24,-18,-20,-21,113,117,-9,-25,-13,-38,132,136,137,138,-10,140,-26,-11,147,148,149,-14,-12,]),'ASPAS':([2,3,16,18,20,21,22,23,34,38,40,42,43,66,67,68,69,70,76,78,80,94,96,97,100,101,102,103,111,113,117,119,136,138,140,148,149,],[-2,-3,-36,-41,-1,-4,-5,-6,-23,-27,60,-7,-8,-19,-15,-16,-17,-22,-28,95,-40,-37,-39,-42,-24,-18,-20,-21,-9,-25,-13,-38,-10,-26,-11,-14,-12,]),'DELIMITADOR':([4,5,6,11,15,45,46,48,49,50,51,52,77,79,81,83,84,85,86,110,],[21,22,23,34,38,-50,-51,66,67,68,69,70,94,96,97,100,101,102,103,119,]),'ABRE_CH':([7,8,],[24,25,]),'FECHA_P':([10,27,28,29,30,31,32,44,53,55,56,59,61,62,64,88,89,90,91,95,120,128,129,130,139,],[-44,45,46,-45,-46,-47,-48,63,71,-35,74,77,79,81,-49,-43,-29,-30,-31,110,126,-32,-33,-34,142,]),'VALOR_NUMINT':([10,33,40,47,65,73,75,122,],[29,49,29,29,85,89,93,128,]),'VALOR_NUMDEC':([10,33,40,47,65,73,123,],[30,50,30,30,86,90,129,]),'VALOR_TEXTO':([10,33,40,47,73,124,],[31,51,31,31,91,130,]),'OP_ATRIBUI':([11,57,],[33,75,]),'ABRE_CLT':([15,45,46,63,71,74,121,126,141,142,],[39,-50,-51,82,87,92,127,87,143,144,]),'FECHA_CH':([24,25,],[42,43,]),'VIRGULA':([28,29,30,31,32,55,59,61,64,88,89,90,91,93,118,128,129,130,],[47,-45,-46,-47,-48,-35,-48,47,47,-43,-29,-30,-31,109,125,-32,-33,-34,]),'DOIS_PONTOS':([29,30,31,32,59,61,64,],[-45,-46,-47,-48,-48,80,-49,]),'OP_ARIT':([48,65,131,135,],[65,84,135,139,]),'OP_REL':([53,54,55,56,88,89,90,91,114,115,116,118,120,128,129,130,],[72,73,-35,72,72,-29,-30,-31,122,123,124,72,72,-32,-33,-34,]),'OP_LOGICO':([89,90,91,],[105,106,107,]),'SENAO':([113,137,],[121,141,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,39,60,87,92,127,144,],[1,58,78,104,108,134,146,]),'statement':([0,1,39,58,60,78,82,87,92,104,108,126,127,134,143,144,146,],[2,20,2,20,2,20,98,2,2,20,20,133,2,20,145,2,20,]),'funcao':([0,1,33,39,58,60,78,82,87,92,104,108,126,127,134,143,144,146,],[15,15,52,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'param_vazio':([10,],[27,]),'param':([10,40,47,],[28,61,64,]),'cond_param':([35,36,72,109,112,],[53,56,88,118,120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements_multiple','main.py',135),
  ('statements -> statement','statements',1,'p_statements_single','main.py',140),
  ('statement -> COMENT','statement',1,'p_statement_comentarios','main.py',145),
  ('statement -> INTERROMPA DELIMITADOR','statement',2,'p_statement_interrompa','main.py',149),
  ('statement -> IFSULDEMINAS DELIMITADOR','statement',2,'p_statement_ifsuldeminas','main.py',155),
  ('statement -> COMPILADORES DELIMITADOR','statement',2,'p_statement_compiladores','main.py',160),
  ('statement -> INICIO ABRE_CH FECHA_CH','statement',3,'p_statement_inicio','main.py',165),
  ('statement -> FIM ABRE_CH FECHA_CH','statement',3,'p_statement_fim','main.py',170),
  ('statement -> DEFINE ABRE_P VAR FECHA_P ABRE_CLT statement FECHA_CLT','statement',7,'p_statement_define','main.py',175),
  ('statement -> DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P FECHA_CLT FECHA_CLT','statement',11,'p_statement_define','main.py',176),
  ('statement -> DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT FECHA_CLT','statement',12,'p_statement_define','main.py',177),
  ('statement -> DEFINE ABRE_P VAR FECHA_P ABRE_CLT SE ABRE_P cond_param FECHA_P statement FECHA_CLT SENAO ABRE_CLT statement FECHA_CLT FECHA_CLT','statement',16,'p_statement_define','main.py',178),
  ('statement -> ENQUANTO ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT','statement',7,'p_statement_enquanto','main.py',183),
  ('statement -> PARA ABRE_P VAR OP_ATRIBUI VALOR_NUMINT VIRGULA cond_param VIRGULA VAR OP_ARIT OP_ARIT FECHA_P ABRE_CLT statements FECHA_CLT','statement',15,'p_statement_para','main.py',189),
  ('statement -> VAR OP_ATRIBUI VALOR_NUMINT DELIMITADOR','statement',4,'p_statement_atribuicaoValorVariavel','main.py',194),
  ('statement -> VAR OP_ATRIBUI VALOR_NUMDEC DELIMITADOR','statement',4,'p_statement_atribuicaoValorVariavel','main.py',195),
  ('statement -> VAR OP_ATRIBUI VALOR_TEXTO DELIMITADOR','statement',4,'p_statement_atribuicaoValorVariavel','main.py',196),
  ('statement -> VAR OP_ATRIBUI VAR OP_ARIT OP_ARIT DELIMITADOR','statement',6,'p_statement_atribuicaoValorVariavel','main.py',197),
  ('statement -> VAR OP_ATRIBUI VAR DELIMITADOR','statement',4,'p_statement_atribuicaoValorVariavel','main.py',198),
  ('statement -> VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMINT DELIMITADOR','statement',6,'p_statement_atribuicaoValorVariavel','main.py',199),
  ('statement -> VAR OP_ATRIBUI VAR OP_ARIT VALOR_NUMDEC DELIMITADOR','statement',6,'p_statement_atribuicaoValorVariavel','main.py',200),
  ('statement -> VAR OP_ATRIBUI funcao DELIMITADOR','statement',4,'p_statement_atribuicaoValorVariavel','main.py',201),
  ('statement -> VAR DELIMITADOR','statement',2,'p_statement_atribuicaoValorVariavel','main.py',202),
  ('statement -> VAR OP_ATRIBUI VAR OP_ARIT VAR DELIMITADOR','statement',6,'p_statement_atribuicaoValorVariavel','main.py',203),
  ('statement -> SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT','statement',7,'p_statement_condicionais','main.py',208),
  ('statement -> SE ABRE_P cond_param FECHA_P ABRE_CLT statements FECHA_CLT SENAO ABRE_CLT statements FECHA_CLT','statement',11,'p_statement_condicionais','main.py',209),
  ('statement -> funcao DELIMITADOR','statement',2,'p_statement_funcao_invocada','main.py',215),
  ('statement -> funcao ABRE_CLT statements FECHA_CLT','statement',4,'p_statement_definir_funcao','main.py',220),
  ('cond_param -> VAR OP_REL VALOR_NUMINT','cond_param',3,'p_parametro_condicional','main.py',225),
  ('cond_param -> VAR OP_REL VALOR_NUMDEC','cond_param',3,'p_parametro_condicional','main.py',226),
  ('cond_param -> VAR OP_REL VALOR_TEXTO','cond_param',3,'p_parametro_condicional','main.py',227),
  ('cond_param -> VAR OP_REL VALOR_NUMINT OP_LOGICO VAR OP_REL VALOR_NUMINT','cond_param',7,'p_parametro_condicional','main.py',229),
  ('cond_param -> VAR OP_REL VALOR_NUMDEC OP_LOGICO VAR OP_REL VALOR_NUMDEC','cond_param',7,'p_parametro_condicional','main.py',230),
  ('cond_param -> VAR OP_REL VALOR_TEXTO OP_LOGICO VAR OP_REL VALOR_TEXTO','cond_param',7,'p_parametro_condicional','main.py',231),
  ('cond_param -> BOOLEANO','cond_param',1,'p_parametro_condicional','main.py',232),
  ('statement -> AUX','statement',1,'p_aux','main.py',236),
  ('statement -> ESCREVA ABRE_P VAR FECHA_P DELIMITADOR','statement',5,'p_impressao','main.py',240),
  ('statement -> ESCREVA ABRE_P ASPAS statements ASPAS FECHA_P DELIMITADOR','statement',7,'p_impressao','main.py',241),
  ('statement -> ESCREVA ABRE_P param FECHA_P DELIMITADOR','statement',5,'p_impressao','main.py',242),
  ('statement -> ESCREVA ABRE_P param DOIS_PONTOS','statement',4,'p_impressao','main.py',243),
  ('statement -> BOOLEANO','statement',1,'p_true_false','main.py',247),
  ('statement -> LEIA ABRE_P VAR FECHA_P DELIMITADOR','statement',5,'p_leitura','main.py',252),
  ('cond_param -> cond_param OP_REL cond_param','cond_param',3,'p_parametros_condicionais_grupo','main.py',258),
  ('param_vazio -> <empty>','param_vazio',0,'p_parametro_vazio','main.py',263),
  ('param -> VALOR_NUMINT','param',1,'p_parametro','main.py',268),
  ('param -> VALOR_NUMDEC','param',1,'p_parametro','main.py',269),
  ('param -> VALOR_TEXTO','param',1,'p_parametro','main.py',270),
  ('param -> VAR','param',1,'p_parametro','main.py',271),
  ('param -> param VIRGULA param','param',3,'p_parametro_grupo','main.py',276),
  ('funcao -> ABRE_P param_vazio FECHA_P','funcao',3,'p_regra_funcao','main.py',281),
  ('funcao -> ABRE_P param FECHA_P','funcao',3,'p_regra_funcao','main.py',282),
]
