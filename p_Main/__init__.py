__all__ = ['m_CenterFrame']

def centralize(child):
    parent = child.parent()
    x = (parent.width() - child.width()) / 2
    y = (parent.height() - child.height()) / 2
    child.move(x,y)