def three(totallist, search_index):
    default_state_agricultural_workers = 'JAMMU & KASHMIR'
    worker_no = 0
    worker_dict = {}
    default_state_mobile_penetration = 'JAMMU & KASHMIR'
    mobile_dict = {}
    mobile_no = 0
    population_agriculture = 0
    population_mobile = 0
    barchart_agriculture = {}
    barchart_mobile = {}
    totaldata = {}
    mobile_penetation = []
    agricultural_workers = []
    slackareachart1 = []
    slackareachart2 = []
    count = 1
    if int(search_index) == 1: 
        for item in totallist:
            for key, value in item.items():
                if key == 'Agricultural_Workers':
                    if default_state_agricultural_workers == item['State name']:
                        worker_no = worker_no + int(item['Agricultural_Workers'])
                        population_agriculture = population_agriculture + int(item['Population'])
                    elif default_state_agricultural_workers != item['State name']:
                        worker_dict['y'] = worker_no
                        worker_dict['label'] = default_state_agricultural_workers
                        barchart_agriculture['y'] = ((float(worker_no) / float(population_agriculture)) * 100)
                        barchart_agriculture['label'] = default_state_agricultural_workers
                        agricultural_workers.append(worker_dict)
                        slackareachart2.append(barchart_agriculture)
                        population_agriculture = 0
                        barchart_agriculture = {}
                        worker_dict = {}
                        default_state_agricultural_workers = item['State name']
                        worker_no = 0
                        worker_no = worker_no + int(item['Agricultural_Workers'])
                        population_agriculture = population_agriculture + int(item['Population'])

                if key == 'Households_with_Telephone_Mobile_Phone_Mobile_only':
                    if default_state_mobile_penetration == item['State name']:
                        mobile_no = mobile_no + int(item['Households_with_Telephone_Mobile_Phone_Mobile_only'])
                        population_mobile = population_mobile + int(item['Population'])
                    elif default_state_mobile_penetration == 'LAKSHADWEEP' and count == 1:
                        Lakshadweep = {'y': 0, 'label': 'LAKSHADWEEP'}
                        agricultural_workers.append(Lakshadweep)
                        slackareachart2.append(Lakshadweep)
                        count = count + 1
                    elif default_state_mobile_penetration != item['State name']:
                        mobile_dict['y'] = mobile_no
                        mobile_dict['label'] = default_state_mobile_penetration
                        barchart_mobile['y'] = ((float(mobile_no) / float(population_mobile)) * 100)
                        barchart_mobile['label'] = default_state_mobile_penetration
                        mobile_penetation.append(mobile_dict)
                        slackareachart1.append(barchart_mobile)
                        population_mobile = 0
                        barchart_mobile = {}
                        mobile_dict = {}
                        default_state_mobile_penetration = item['State name']
                        mobile_no = 0
                        mobile_no = mobile_no + int(item['Households_with_Telephone_Mobile_Phone_Mobile_only'])
                        population_mobile = population_mobile + int(item['Population'])

    elif int(search_index) == 2:
        for item in totallist:
            for key, value in item.items():
                if key == 'Households_with_Telephone_Mobile_Phone_Mobile_only':
                    mp = {}
                    sac1 = {}
                    mp['label'] = item['District name']
                    mp['y'] = int(item['Households_with_Telephone_Mobile_Phone_Mobile_only'])
                    sac1['y'] = (float(item['Households_with_Telephone_Mobile_Phone_Mobile_only']) / float(item['Population'])) * 100
                    sac1['label'] = item['District name']
                    mobile_penetation.append(mp)
                    slackareachart1.append(sac1)

                elif key == 'Agricultural_Workers':
                    aw = {}
                    sac2 = {}
                    aw['label'] = item['District name']
                    aw['y'] = int(item['Agricultural_Workers'])
                    sac2['y'] = (float(item['Agricultural_Workers']) / float(item['Population'])) * 100
                    sac2['label'] = item['District name']
                    agricultural_workers.append(aw)
                    slackareachart2.append(sac2)
        Lakshadweep = {'y': 0, 'label': 'Lakshadweep'}
        agricultural_workers.append(Lakshadweep)
        slackareachart2.append(Lakshadweep)

    else:
        pass

    totaldata['mobile'] = mobile_penetation
    totaldata['agriculture'] = agricultural_workers
    totaldata['mobileareachart1'] = slackareachart1
    totaldata['agricultureareachart2'] = slackareachart2

    return totaldata


def one(totallist, thresold):
    bar_chart_value_dict = {}
    low_literacy_rates = []
    bar_chart_value = []
    highrate = []
    lowrate = []
    default_state = 'JAMMU & KASHMIR'
    x = 0
    y = 0
    list_of_particular_state = []
    for dictionary in totallist:
        for key, value in dictionary.items():
            if default_state == dictionary['State name']:
                x = x + int(dictionary['Literate'])
                y = y + int(dictionary['Population'])
            if default_state != dictionary['State name']:
                list_of_particular_state.append(default_state)
                list_of_particular_state.append(x)
                list_of_particular_state.append(y)
                low_literacy_rates.append(list_of_particular_state)
                list_of_particular_state = []
                x = 0
                y = 0
                default_state = dictionary['State name']
                x = x + int(dictionary['Literate'])
                y = y + int(dictionary['Population'])

    for item in low_literacy_rates:
        literacy_rate = (float(item[1])/float(item[2]))*100
        per_item_rate = []
        per_item_rate.append(item[0])
        per_item_rate.append(literacy_rate)
        bar_chart_value.append(per_item_rate)

    for item in bar_chart_value:
        if int(item[1]) < int(thresold):
            first = {}
            first['y'] = item[1]
            first['label']=item[0]
            highrate.append(first)
        elif int(item[1]) >= int(thresold):
            second = {}
            second['y'] = item[1]
            second['label']=item[0]
            lowrate.append(second)
        else:
            pass

    bar_chart_value_dict['upper'] = highrate
    bar_chart_value_dict['lower'] = lowrate

    return bar_chart_value_dict


def two(totallist, search_index):
    bihar = []
    tamilnadu = []
    final_list = {}
    chart1 = []
    chart2 = []

    for each_list in totallist:
                for key, value in each_list.items():
                    if key == 'State name':
                        if value == 'BIHAR':
                            bihar.append(each_list)
                        elif value == 'TAMIL NADU':
                            tamilnadu.append(each_list)

    dev = 0.008
    for item1 in bihar:
        for key, value in item1.items():
            if key == search_index:
                for item2 in tamilnadu:
                    for k, v in item2.items():
                        if k == search_index:
                            val = int(v) * dev
                            lower_value = int(v) - val
                            upper_value = int(v) + val
                            if int(value) > int(lower_value) and int(value) < int(upper_value):
                                each_district_of_bihar = {}
                                each_district_of_tamilnadu = {}
                                each_district_of_bihar['label'] = item1['District name']
                                each_district_of_bihar['y'] = int(item1[search_index])
                                chart1.append(each_district_of_bihar)
                                each_district_of_tamilnadu['label'] = item2['District name']
                                each_district_of_tamilnadu['y'] = int(item2[search_index])
                                chart2.append(each_district_of_tamilnadu)

    final_list['BIHAR'] = chart1
    final_list['TAMIL_NADU'] = chart2
    return final_list












    





  