# Design Patterns in Python

A learning set of design-pattern examples in Python, based on the Stepik course [[GG Python] Паттерны ООП в Python: Продвинутый уровень](https://stepik.org/course/277065/syllabus).

Patterns here are not ready-made libraries. They are repeatable ways to solve architectural problems. The classification helps you pick a tool for the job: one pattern governs how objects are **created**, another how they are **composed**, and a third how they **communicate**.

In Python this classification is especially useful. Dynamic typing, functions and classes as first-class objects, duck typing, `@` decorators, and modules as singleton objects let you implement many Gang of Four (GoF) patterns in a few lines, where C++ or Java would need a full class hierarchy. That is why this set covers both the classic groups and Pythonic additions.

Examples live in [`patterns/`](patterns/) and are grouped by category. ✅ marks patterns that have examples in this repository. ❌ marks the rest of the classification.

## The three GoF pillars

The Gang of Four book *Design Patterns* (1994) defined 23 patterns in three categories.

### Creational

These patterns create objects flexibly and hide instantiation from client code.

| Pattern | Idea | Examples |
| --- | --- | --- |
| ✅ Singleton | Guarantees a single instance and a global access point. In Python it is often replaced by a module or a class with a custom `__new__` | see [Global Object](patterns/pythonic_architecture/global_object/) |
| ✅ Factory Method | Delegates object creation to subclasses, which decide which concrete object to build | [`factory_method/`](patterns/creational/factory_method/) |
| ✅ Abstract Factory | Creates families of related objects (for example, UI components for different operating systems) without binding client code to concrete classes | [`abstract_factory_python/`](patterns/creational/abstract_factory_python/) |
| ✅ Builder | Assembles a complex object step by step when it has many optional parameters. In Python a fluent interface or a dataclass with `__post_init__` fits well | [`builder/`](patterns/creational/builder/) |
| ❌ Prototype | Creates a new object by cloning an existing instance (`copy.deepcopy()`). In Python, functions and classes are already first-class objects, so a dedicated pattern is usually unnecessary | — |

### Structural

These patterns compose classes and objects, building larger structures out of smaller parts.

| Pattern | Idea | Examples |
| --- | --- | --- |
| ✅ Adapter | Adapts an incompatible interface to the one a client expects. Delegation or inheritance is often enough | [`adapter/`](patterns/structural/adapter/) |
| ❌ Bridge | Separates an abstraction from its implementation so the two can change independently. Useful when one piece of logic has several backends; rare in its pure form | — |
| ✅ Composite | Groups objects into a tree so a client can treat a single object and a composite the same way | [`composite/`](patterns/structural/composite/) |
| ✅ Decorator | Adds new behavior to an object dynamically | [`decorator/`](patterns/structural/decorator/) |
| ✅ Facade | Offers one simple interface to a complex subsystem and hides its internals | [`facade/`](patterns/structural/facade/) |
| ❌ Flyweight | Shares fine-grained objects to save memory by keeping extrinsic state outside the object. Python uses this for string literals and small integers; it is rare in application code | — |
| ✅ Proxy | Controls access to another object: lazy initialization, protection, logging, or remote access | [`proxy/`](patterns/structural/proxy/) |

### Behavioral

These patterns define algorithms and the ways objects communicate, splitting responsibility among them.

| Pattern | Idea | Examples |
| --- | --- | --- |
| ✅ Chain of Responsibility | Passes a request along a chain of handlers until one of them handles it | [`chain_of_responsibility/`](patterns/behavioral/chain_of_responsibility/) |
| ✅ Command | Wraps a request in an object so clients can be parameterized, operations queued, and actions undone | [`command/`](patterns/behavioral/command/) |
| ❌ Interpreter | Represents a language grammar and interprets sentences through a class hierarchy. Rarely used in its pure form | — |
| ❌ Iterator | Provides sequential access to a collection without exposing its structure. In Python this is `__iter__` and `__next__` | — |
| ❌ Mediator | Centralizes complex interactions among many objects. Usually replaced by Observer | — |
| ❌ Memento | Saves and restores an object's internal state without breaking encapsulation. Redundant in Python: `pickle` serializes an object, `copy.deepcopy` copies it, and undo is usually done with Command | — |
| ✅ Observer | A one-to-many dependency: when the subject changes, every observer is notified | [`observer/`](patterns/behavioral/observer/) |
| ✅ State | Changes an object's behavior when its internal state changes, so it looks as if the object changed its class | [`state/`](patterns/behavioral/state/) |
| ✅ Strategy | A family of interchangeable algorithms, each encapsulated on its own | [`strategy/`](patterns/behavioral/strategy/) |
| ✅ Template Method | Defines the skeleton of an algorithm in a base class and lets subclasses override individual steps | [`template_method/`](patterns/behavioral/template_method/) |
| ❌ Visitor | Separates an algorithm from the object structure it works on, adding operations without changing the element classes. In Python, dynamic typing, `singledispatch`, `match`/`case`, and ordinary class extension replace its double dispatch | — |

## Pythonic and architectural additions

Beyond the classics, the Python ecosystem has patterns that either change a lot under the language's dynamics or come from enterprise and web architecture.

| Pattern | Idea | Examples |
| --- | --- | --- |
| ✅ Object Pool | Keeps a set of pre-created objects, lends them out, and takes them back. Needed for expensive resources: database connections, sockets, heavy models | [`object_pool/`](patterns/pythonic_architecture/object_pool/) |
| ✅ Repository | Hides data access behind a collection-like interface over a database, an API, or the filesystem. Central to clean architecture and [DDD](https://en.wikipedia.org/wiki/Domain-driven_design) | [`repository/`](patterns/pythonic_architecture/repository/) |
| ❌ Unit of Work | Tracks object changes inside a business transaction and commits them together | — |
| ❌ Data Mapper | Moves data between objects and storage without tying the domain model to the database schema | — |
| ✅ Dependency Injection | Passes dependencies into an object from the outside instead of letting the object create them. In Python this is a constructor, a factory, or a framework such as `dependency-injector` | — |
| ✅ Sentinel Object | A unique token meaning "no value" in places where `None` can be valid data. Used by `functools.lru_cache` and configuration parsers | [`sentinel/`](patterns/pythonic_architecture/sentinel/) |
| ❌ Borg (Monostate) | Every instance of a class shares one `__dict__` while remaining a distinct object. A Python alternative to Singleton; this set uses Global Object instead | — |
| ✅ Global Object | A module or a module-level variable. Import gives a single instance in a Pythonic way and often replaces the classic Singleton | [`global_object/`](patterns/pythonic_architecture/global_object/) |
| ✅ Prebound Method | Exports an object's method as a module function and keeps shared state through an instance created in advance | [`prebound_method/`](patterns/pythonic_architecture/prebound_method/) |

## In practice

Patterns rarely stand alone. A Repository often relies on Unit of Work and Data Mapper, a Decorator can wrap objects from an Object Pool, and Strategy in Python is usually a prebound method rather than a class hierarchy.

The goal is to know which group to search when you need more flexibility in how objects are **created**, **composed**, or how they **communicate**.
