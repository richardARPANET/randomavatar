from randomavatar.randomavatar import Avatar


def main():
    # Example usage
    avatar = Avatar(rows=10, columns=10)
    image_byte_array = avatar.get_image(string='john_smith_2008',
                                        width=400,
                                        height=400,
                                        pad=10)

    return avatar.save(image_byte_array=image_byte_array,
                       save_location='example.png')

if __name__ == '__main__':
    main()
