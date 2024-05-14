package org.acvy.gsteam.entities;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.Id;


@Setter @Getter
@NoArgsConstructor @AllArgsConstructor
@Entity
public class Product {
    @Id private Long id;
    private String name;
    private String description;
    private String image;
    private String genre;
    private String price;

    Product(Product other)
    {
        this.id = other.id;
        this.name = other.name;
        this.description = other.description;
        this.image = other.image;
        this.genre = other.genre;
        this.price = other.price;
    }
}
