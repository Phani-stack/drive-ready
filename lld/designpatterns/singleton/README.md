# Singleton Design Principle

One object for overall system. When one service used by all the other servies, it needs a single object then we apply singleton.

**examples**

- logger
- database connetion manager
- config classes

### Questions before Singleton

1. What does this class actually do ?
2. Do many parts of application need it ?
3. Do they need same instance ?

### Advantages of Singleton

1. Saves memory.
2. Prevents unnecessary object creation.

3. Any part of the application can access the same object.
4. Same data everywhere
5. Since everyone uses the same object, its state is shared.
6. One configuration object used throughout the application.
7. Useful for shared resources
8. The class itself ensures that nobody creates multiple instances.
9. Good for things where you logically need only one instance:
   - Application configuration
   - Logger
   - Cache manager
   - Connection/resource manager
   - System settings
