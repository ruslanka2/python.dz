import view
import gui
import logs

def button_click():
    value_a=view.get_value()
    op=view.get_operation()
    value_b=view.get_value()
    func=gui.dict_ar[op]
    func.init(value_a,value_b)
    result = func.do_it()
    view.get_resultat(result)
    operation = gui.dict_log[op]
    logs.get_log(result, operation)