import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("Fileio/recipies", writeback=True) as recipies:
    # recipies['blt'] = blt
    # recipies['beans_on_toast'] = beans_on_toast
    # recipies['scrambled_eggs'] = scrambled_eggs
    # recipies['soup'] = soup
    # recipies['pasta'] = pasta

    # recipies["blt"].append("butter")
    # recipies["pasta"].append("tomato")

    # temp_list = recipies["blt"]
    # temp_list.append("butter")
    # recipies["blt"] = temp_list

    # temp_list = recipies["pasta"]
    # temp_list.append("tomato")
    # recipies["pasta"] = temp_list
    # recipies['soup'].append('croutons')

    recipies['soup'] = soup
    recipies.sync()
    soup.append('cream')

    for snack in recipies:
        print(snack, recipies[snack])
