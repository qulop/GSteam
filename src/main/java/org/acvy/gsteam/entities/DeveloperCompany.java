package org.acvy.gsteam.entities;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
@Entity @Table(name = "developer_company")
public class DeveloperCompany {
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String name;

    public DeveloperCompany(String name) {
        this.name = name;
    }

    public DeveloperCompany(DeveloperCompany other) {
        this.id = other.id;
        this.name = other.name;
    }
}
