from functools import partial

import re
import logging
import pymel.core as pm


# -- Constants
option_var_dict = pm.OptionVarDict()


# -- Regex pattern to find optionVariables by
regex_pattern = re.compile(
    '^playback.*'
)


def set_option_var_value(key, value):
    """
    Command for changing the option variable from the Ui.
    
    :param key: OptionVar key name.
    :type key: str
    
    :param value: OptionVar key value.
    :type value: int / float / str
    
    :return: None
    """
    option_var_dict[key] = value
    logging.info('Changed %s to %s' % (key, value))


def main():
    """
    Simple Ui to manage option variables.
    """
    # -- Sorted startup names
    matching_variables = sorted(
        var
        for var in option_var_dict.keys()
        if regex_pattern.match(var)
    )
    
    win_name = 'optionvar_editor_win'
    
    # -- Delete window if it already exists
    if pm.window(win_name, ex=True):
        pm.deleteUI(win_name)
    
    # -- Recreate the Ui
    with pm.window(win_name) as win:
        with pm.columnLayout(adj=True):
            pm.text('Edit Option Variables', h=25)
            pm.separator(h=10)
            
            with pm.scrollLayout():
                with pm.columnLayout(adj=True):
                    
                    # -- Generate row for each valid variable
                    for var in matching_variables:
                        
                        # -- Get value
                        val = option_var_dict[var]
                        
                        # -- Skip unsupported types
                        if not isinstance(val, (str,
                                                unicode,
                                                int,
                                                float)):
                            logging.warning(
                                'Unable to display unknown type %s (%s)' % (val,
                                                                            str(type(val)))
                            )
                            continue
                        
                        with pm.rowLayout(adj=1, nc=2):
                            
                            # -- Create a label
                            pm.text(
                                '%s: ' % var,
                                align='right',
                            )
                            
                            # -- Create a textfield to show text
                            if isinstance(val, (str, unicode)):
                                pm.textField(
                                    text=val,
                                    annotation='Original value: %s' % val,
                                    enterCommand=partial(
                                        set_option_var_value,
                                        var,
                                    ),
                                )
                            
                            # -- Create a float field to show float
                            elif isinstance(val, float):
                                pm.floatField(
                                    value=val,
                                    width=100,
                                    annotation='Original value: %s' % val,
                                    changeCommand=partial(
                                        set_option_var_value,
                                        var,
                                    ),
                                )
                            
                            # -- Create an int field to show integer
                            elif isinstance(val, int):
                                pm.intField(
                                    value=val,
                                    width=100,
                                    annotation='Original value: %s' % val,
                                    changeCommand=partial(
                                        set_option_var_value,
                                        var,
                                    ),
                                )
        
        # -- Show the Ui
        win.show()


def onMayaDroppedPythonFile(*args):
    """
    Drag n Drop command when .py files are dropped
    into the scene.
    
    :return: None
    """
    main()


if __name__ == '__main__':
    main()
