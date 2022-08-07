
def get_items(items):
    items_list = []
    for item in items:
        items_list.append({ 'id': item.id , 'name': item.name })
    return items_list

def categories_material(categories, materials):
    return {
        'categories': get_items(categories),
        'materials': get_items(materials)
    }
        
    