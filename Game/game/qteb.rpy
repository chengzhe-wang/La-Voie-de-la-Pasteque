label qte_setup1(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_button
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not

    return


screen qte_button:

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])
    #see above

    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1)
            xalign 0.3
            xysize 100, 100
            background Animation("square")


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.5):
                left_bar "#f00"
