package org.acvy.gsteam.reps;

import org.acvy.gsteam.entities.GameProduct;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface ProductRepository extends JpaRepository<GameProduct, Long> {

}
