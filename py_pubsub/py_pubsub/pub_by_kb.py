import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .getchar import Getchar

class Pub_by_kb(Node):

    def __init__(self):
        super().__init__('Pub_by_kb')
        self.pub = self.create_publisher(String, 'control', 10)


def main(args=None):
    rclpy.init(args=args)

    node = Pub_by_kb()
    kb = Getchar()
    msg = String()
    try:
        while rclpy.ok():
        
            key = kb.getch()
        
            if key == '1':
                msg.data = 'message1'
            elif key == '2':
                msg.data = 'message2'
            elif key == '3':
                msg.data = 'message3'
            else:
                pass
                
            node.pub.publish(msg)
    except KeyboardInterrupt:
            
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
