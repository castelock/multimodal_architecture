from interaction_manager import InteractionManager
from threading import Thread


interact_manager = InteractionManager()

#t1 = Thread(target=interact_manager.activateUI, daemon=True)
t2 = Thread(target=interact_manager.activateGestureInteraction, daemon=True)

#t1.start()
t2.start()

interact_manager.activateUI()


"""interact_manager.activateUI()
interact_manager.activateGestureInteraction()"""