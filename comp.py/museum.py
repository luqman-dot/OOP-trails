class Artifact:
    def __init__(self, name, age, origin, description):
        self.name = name
        self.age = age
        self.origin = origin
        self.description = description

    def display_info(self):
        return f"""
        Name: {self.name}
        Age: {self.age} years
        Origin: {self.origin}
        Description: {self.description}
        """


class Museum:
    def __init__(self):
        self.artifacts = []

    def add_artifact(self, artifact):
        self.artifacts.append(artifact)
        print(f"Artifact '{artifact.name}' has been added to the catalog.")

    def view_artifacts(self):
        if not self.artifacts:
            print("No artifacts in the catalog yet.")
        else:
            for i, artifact in enumerate(self.artifacts, start=1):
                print(f"Artifact {i}:\n{artifact.display_info()}")

    def search_artifact(self, keyword):
        results = [artifact for artifact in self.artifacts if keyword.lower() in artifact.name.lower()]
        if not results:
            print(f"No artifacts found matching '{keyword}'.")
        else:
            print(f"Search results for '{keyword}':")
            for artifact in results:
                print(artifact.display_info())


def main():
    museum = Museum()

    while True:
        print("\nMuseum Artifact Catalog")
        print("1. Add Artifact")
        print("2. View All Artifacts")
        print("3. Search Artifact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter artifact name: ")
            age = input("Enter artifact age (in years): ")
            origin = input("Enter artifact origin: ")
            description = input("Enter artifact description: ")
            artifact = Artifact(name, age, origin, description)
            museum.add_artifact(artifact)

        elif choice == "2":
            museum.view_artifacts()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            museum.search_artifact(keyword)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
