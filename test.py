call_info = {
    0:{
        "start":1
    },

    1:{
        "start":2
    },

    3:{
        "start":5
    },

    6:{
        "start":10
    }
}

enter_l = [0,1,3,6]

ch = [k for k,v in zip(call_info.keys(),call_info.values())]

print(ch)