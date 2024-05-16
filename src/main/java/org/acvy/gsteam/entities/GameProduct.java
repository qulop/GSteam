package org.acvy.gsteam.entities;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;


@Setter @Getter
@NoArgsConstructor @AllArgsConstructor
@Entity @Table(name = "game_product")
public class GameProduct {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private Float price;
    private Short score;
    @OneToMany @JoinColumn(name = "developer_id")
    private DeveloperCompany developer_id;

    public GameProduct(String title, Float price, Short score, DeveloperCompany developer_id) {
        this.title = title;
        this.price = price;
        this.score = score;
        this.developer_id = developer_id;
    }

    public GameProduct(GameProduct other)
    {
        this.id = other.id;
        this.title = other.title;
        this.price = other.price;
        this.score = other.score;
        this.developer_id = other.developer_id;
    }
}
